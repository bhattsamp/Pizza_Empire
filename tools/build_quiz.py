# Converts every CSV in in/ into per-subject JS data files: out/quiz/sNN.js + out/quiz/index.js
import csv,glob,json,os,collections
SUBJ=["IQ & Logical Reasoning","Mathematics","General Knowledge","Business & Finance","Detective & Mystery","Science & Technology","Geography","History","Word & Language","Engineering & Mechanics","Memory & Observation","Coding & Programming","Architecture & Design","Food & Cooking","Agriculture & Farming","Space & Astronomy","Environmental Science","Business Negotiation","Traffic & Parking","Escape Room","Pattern Recognition","Brain Teasers","Physics Challenges","Chemistry Puzzles","Biology & Human Body","Computer Knowledge","Art & Creativity","Sports Trivia","Music & Sound Recognition","Animal & Wildlife Knowledge","History of Inventions","Financial Literacy","Marketing & Sales","Real Estate Knowledge","Customer Service Challenges","Strategy & Decision Making","Code Breaking","Shape & Colour Matching","Word Search & Crossword","Building & Construction Puzzles","Mythology"]
data=collections.defaultdict(lambda:collections.defaultdict(dict)); problems=[]
for f in sorted(glob.glob('in/*.csv')):
    for r in csv.DictReader(open(f,encoding='utf-8-sig')):
        try:
            sid=int(r['subject_id']);lv=int(r['level']);qn=int(r['qno'])
            ci='ABCD'.index(r['correct'].strip().upper())
            q=[r['question'].strip()]+[r['option_'+k].strip() for k in 'abcd']+[ci,r['explanation'].strip()]
            if not all(q[:5]) or len(set(q[1:5]))<4: raise ValueError('empty/duplicate option')
            data[sid][lv][qn]=q
        except Exception as e: problems.append((f,r.get('subject_id'),r.get('level'),r.get('qno'),str(e)))
os.makedirs('out/quiz',exist_ok=True)
index={}
for sid,levels in data.items():
    full={lv:[qs[k] for k in sorted(qs)] for lv,qs in levels.items() if len(qs)==21}
    for lv,qs in levels.items():
        if len(qs)!=21: problems.append(('level incomplete',sid,lv,len(qs)))
    index[sid]=sorted(full)
    open(f'out/quiz/s{sid:02d}.js','w',encoding='utf-8').write('QZ.reg(%d,%s);'%(sid,json.dumps({str(k):v for k,v in full.items()},ensure_ascii=False,separators=(',',':'))))
open('out/quiz/index.js','w').write('window.QZI=%s;'%json.dumps({str(k):v for k,v in sorted(index.items())},separators=(',',':')))
print('subjects',{k:len(v) for k,v in sorted(index.items())},'problems',problems[:10],len(problems))
