import 'package:flutter/material.dart';
import 'package:flutter/services.dart';
import 'package:webview_flutter/webview_flutter.dart';
import 'package:webview_flutter_android/webview_flutter_android.dart';

/// Pizza Empire – Merge & Cook
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
      title: 'Pizza Empire',
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

  @override
  void initState() {
    super.initState();
    WidgetsBinding.instance.addObserver(this);

    _controller = WebViewController()
      ..setJavaScriptMode(JavaScriptMode.unrestricted)
      ..setBackgroundColor(const Color(0xFF2B1A10))
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
        backgroundColor: const Color(0xFF2B1A10),
        body: SafeArea(
          child: Stack(
            children: [
              WebViewWidget(controller: _controller),
              if (_loading)
                Container(
                  color: const Color(0xFFD7263D),
                  alignment: Alignment.center,
                  child: const Column(
                    mainAxisSize: MainAxisSize.min,
                    children: [
                      Text('🍕', style: TextStyle(fontSize: 96)),
                      SizedBox(height: 12),
                      Text(
                        'PIZZA EMPIRE',
                        style: TextStyle(
                          color: Colors.white,
                          fontSize: 32,
                          fontWeight: FontWeight.w900,
                          letterSpacing: 1,
                        ),
                      ),
                      SizedBox(height: 20),
                      CircularProgressIndicator(color: Colors.white),
                    ],
                  ),
                ),
            ],
          ),
        ),
      ),
    );
  }
}
