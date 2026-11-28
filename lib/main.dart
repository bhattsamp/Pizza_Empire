import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:webview_flutter_android/webview_flutter_android.dart';

/// Fun Empire – Pizza Rush, Ludo, Saap Seedi, Mind Empire, Quiz Empire
/// The whole game (100 stages, 3D restaurant, save system) lives in
/// assets/game/index.html and runs offline inside a full-screen WebView.
Future<void> main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await SystemChrome.setPreferredOrientations([DeviceOrientation.portraitUp]);
  await SystemChrome.setEnabledSystemUIMode(SystemUiMode.immersiveSticky);
  runApp(const PizzaEmpireApp());
}

class PizzaEmpireApp extends StatelessWidget {
  const PizzaEmpireApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Fun Empire',
      debugShowCheckedModeBanner: false,
      home: GameScreen(),
    );
  }
}

class GameScreen extends StatefulWidget {
  const GameScreen({super.key});

  @override
  State<GameScreen> createState() => _GameScreenState();
}

class _GameScreenState extends State<GameScreen> with WidgetsBindingObserver {
  late final WebViewController _controller;
  bool _loading = true;
  bool _minTimeDone = false;

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);
    // Show the loading art for at least 2.5 s so the bar can fill.
    Future.delayed(const Duration(milliseconds: 2500), () {
      if (mounted) setState(() => _minTimeDone = true);
    });

    _controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0xFF2B1A10))
      // Study Abroad guide: open official visa websites in an in-app popup.
      ..addJavaScriptChannel('OfficialSite', onMessageReceived: (msg) {
        final url = msg.message;
        if (!url.startsWith('https://') || !mounted) return;
        Navigator.of(context).push(MaterialPageRoute(
          fullscreenDialog: true,
          builder: (_) => OfficialSiteScreen(url: url),
        ));
      })
      ..setNavigationDelegate(
        NavigationDelegate(
          onPageFinished: (_) {
            if (mounted) setState(() => _loading = false);
          },
          // Keep players inside the game; open nothing external.
          onNavigationRequest: (req) => req.url.startsWith('file:') ||
                  req.url.startsWith('about:')
              ? NavigationDecision.navigate
              : NavigationDecision.prevent,
        ),
      );

    final platform = _controller.platform;
    if (platform is AndroidWebViewController) {
      // Allow game sound effects and keep the layout unaffected by
      // the phone's system font size.
      platform.setMediaPlaybackRequiresUserGesture(false);
      platform.setTextZoom(100);
    }

    _controller.loadFlutterAsset('assets/game/index.html');
  }

  @override
  void dispose() {
    WidgetsBinding.instance.removeObserver(this);
    super.dispose();
  }

  /// Android back button: let the game decide (close dialog, pause, go back
  /// a screen). Only exit the app when the game is on its first screen.
  Future<void> _handleBack() async {
    try {
      final result =
          await _controller.runJavaScriptReturningResult('appBack()');
      if (result.toString().contains('exit')) {
        await SystemNavigator.pop();
      }
    } catch (_) {
      await SystemNavigator.pop();
    }
  }

  @override
  Widget build(BuildContext context) {
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) {
        if (!didPop) _handleBack();
      },
      child: Scaffold(
        backgroundColor: const Color(0xFFFF5A5F),
        body: SafeArea(
          child: Stack(
            children: [
              WebViewWidget(controller: _controller),
              IgnorePointer(
                ignoring: !(_loading || !_minTimeDone),
                child: AnimatedOpacity(
                  opacity: (_loading || !_minTimeDone) ? 1 : 0,
                  duration: const Duration(milliseconds: 450),
                  curve: Curves.easeOut,
                  child: const LoadingScreen(),
                ),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

/// Loading screen: Bold FE artwork with an animated progress bar.
class LoadingScreen extends StatelessWidget {
  const LoadingScreen({super.key});

  @override
  Widget build(BuildContext context) {
    return Container(
      color: const Color(0xFFFF5A5F),
      child: Stack(
        fit: StackFit.expand,
        children: [
          Image.asset('assets/splash/loading.jpg',
              fit: BoxFit.cover, alignment: Alignment.topCenter),
          Align(
            alignment: const Alignment(0, 0.82),
            child: TweenAnimationBuilder<double>(
              tween: Tween(begin: 0, end: 1),
              duration: const Duration(milliseconds: 2400),
              curve: Curves.easeInOut,
              builder: (context, v, _) => Padding(
                padding: const EdgeInsets.symmetric(horizontal: 40),
                child: Column(
                  mainAxisSize: MainAxisSize.min,
                  children: [
                    const Text(
                      'Loading...',
                      style: TextStyle(
                        color: Colors.white,
                        fontSize: 26,
                        fontWeight: FontWeight.w900,
                        shadows: [Shadow(color: Colors.black54, blurRadius: 6, offset: Offset(0, 2))],
                      ),
                    ),
                    const SizedBox(height: 10),
                    Container(
                      height: 30,
                      padding: const EdgeInsets.all(4),
                      decoration: BoxDecoration(
                        color: const Color(0x668A1240),
                        borderRadius: BorderRadius.circular(18),
                        border: Border.all(color: Colors.white, width: 3),
                      ),
                      child: Stack(
                        children: [
                          FractionallySizedBox(
                            widthFactor: v.clamp(0.02, 1.0),
                            child: Container(
                              decoration: BoxDecoration(
                                borderRadius: BorderRadius.circular(14),
                                gradient: const LinearGradient(
                                  colors: [Color(0xFFFFFFFF), Color(0xFFFFE0B2)],
                                ),
                              ),
                            ),
                          ),
                          Align(
                            alignment: Alignment.centerRight,
                            child: Padding(
                              padding: const EdgeInsets.only(right: 10),
                              child: Text(
                                '${(v * 100).round()}%',
                                style: const TextStyle(
                                  color: Color(0xFF8A1240),
                                  fontWeight: FontWeight.w900,
                                  fontSize: 15,
                                ),
                              ),
                            ),
                          ),
                        ],
                      ),
                    ),
                  ],
                ),
              ),
            ),
          ),
        ],
      ),
    );
  }
}


/// Full-screen popup browser for official government visa websites.
class OfficialSiteScreen extends StatefulWidget {
  const OfficialSiteScreen({super.key, required this.url});
  final String url;

  @override
  State<OfficialSiteScreen> createState() => _OfficialSiteScreenState();
}

class _OfficialSiteScreenState extends State<OfficialSiteScreen> {
  late final WebViewController _web;
  int _progress = 0;

  @override
  void initState() {
    super.initState();
    _web = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setNavigationDelegate(NavigationDelegate(
        onProgress: (p) {
          if (mounted) setState(() => _progress = p);
        },
        // Stay on secure web pages only.
        onNavigationRequest: (req) => req.url.startsWith('https://')
            ? NavigationDecision.navigate
            : NavigationDecision.prevent,
      ))
      ..loadRequest(Uri.parse(widget.url));
  }

  Future<bool> _goBackInPage() async {
    if (await _web.canGoBack()) {
      await _web.goBack();
      return true;
    }
    return false;
  }

  @override
  Widget build(BuildContext context) {
    final host = Uri.parse(widget.url).host;
    return PopScope(
      canPop: false,
      onPopInvokedWithResult: (didPop, _) async {
        if (didPop) return;
        if (!await _goBackInPage() && context.mounted) {
          Navigator.of(context).pop();
        }
      },
      child: Scaffold(
        backgroundColor: Colors.white,
        appBar: AppBar(
          backgroundColor: const Color(0xFF0D47A1),
          foregroundColor: Colors.white,
          leading: IconButton(
            icon: const Icon(Icons.close),
            onPressed: () => Navigator.of(context).pop(),
          ),
          title: Column(
            crossAxisAlignment: CrossAxisAlignment.start,
            children: [
              const Text('Official website',
                  style: TextStyle(fontSize: 16, fontWeight: FontWeight.w800)),
              Text('🔒 $host',
                  style: const TextStyle(fontSize: 12, color: Colors.white70)),
            ],
          ),
          bottom: PreferredSize(
            preferredSize: const Size.fromHeight(3),
            child: _progress < 100
                ? LinearProgressIndicator(
                    value: _progress / 100,
                    minHeight: 3,
                    backgroundColor: Colors.white24,
                    color: const Color(0xFFFFCA28))
                : const SizedBox(height: 3),
          ),
        ),
        body: SafeArea(child: WebViewWidget(controller: _web)),
      ),
    );
  }
}
