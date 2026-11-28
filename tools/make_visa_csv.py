import csv
S=[]
# Stage 1 – basics of studying abroad
S.append([
("What is a student visa?","Permission to enter a country to study",["A university degree","A bank account","A travel ticket"],"A student visa lets you enter and stay in another country for full-time study."),
("Which document do you usually need FIRST before applying for a student visa?","An admission or offer letter from a school",["A job contract","A driving licence","A hotel booking"],"Almost every country asks for proof that a recognised school has accepted you."),
("What does 'proof of funds' mean?","Evidence you have enough money for fees and living costs",["A list of your hobbies","Your exam marks","A letter from a friend"],"Embassies check you can pay for your studies and life without relying on illegal work."),
("Which document must be valid for travel abroad?","Passport",["Library card","School ID","Ration card"],"Many countries want your passport to stay valid for some months beyond your planned stay."),
("What are 'biometrics' in a visa application?","Fingerprints and a photo of your face",["Your blood group report","Your school marks","Your bank PIN"],"Biometrics prove your identity and are collected at visa centres or by official apps."),
("Which is the SAFEST place to check visa rules?","The official government immigration website",["A random social media post","A friend's old advice","An unknown agent's poster"],"Rules and fees change often, so official sites have the latest information."),
("What should you NEVER submit with a visa application?","Fake documents",["Your passport","Your admission letter","Your bank statement"],"Fake documents can lead to refusal and even a ban from applying again."),
("What does IELTS mainly test?","English language skills",["Maths skills","Computer coding","Sports fitness"],"IELTS, TOEFL and PTE are common English tests accepted for study visas."),
("Why do many countries ask for health insurance for students?","To cover medical costs during your stay",["To pay your tuition","To buy your flight","To rent a car"],"Medical treatment abroad can be very expensive, so insurance is often compulsory."),
("What is an 'SOP' often asked for in study applications?","Statement of Purpose",["Student Office Pass","Special Order Payment","School Opening Plan"],"An SOP explains why you chose the course and how it fits your future plans."),
("What is a visa interview?","A meeting where an officer asks about your study plans",["A job interview","An entrance exam","A medical test"],"Officers check that you are a genuine student with clear plans and funds."),
("What does 'genuine student' mean to a visa officer?","Your main purpose is really to study",["You have many friends abroad","You have travelled a lot","You are very rich"],"Countries like Australia formally test whether applicants truly intend to study."),
("Who usually issues the admission letter?","The college or university",["The embassy","The airline","Your bank"],"Schools issue offers; the government immigration department issues the visa."),
("What is an education loan 'sanction letter'?","A bank letter confirming your loan is approved",["A fine for late payment","A university rule book","A visa refusal letter"],"Many embassies accept loan sanction letters as part of your proof of funds."),
("Which of these is usually NOT a reason for visa refusal?","Liking sports",["Not enough money","Fake documents","Unclear study plans"],"Common refusal reasons are weak finances, unclear plans and false information."),
("When should you usually start your visa process?","Several months before the course starts",["The day before the flight","After the course starts","Only after arriving abroad"],"Processing can take weeks or months, so early applications are safer."),
("What does 'apostille' on a document mean?","An official certificate confirming the document is genuine for use abroad",["A type of passport","A school grade","A bank fee"],"Countries in the Hague Apostille Convention accept apostilled documents from each other."),
("What is a 'police clearance certificate'?","A document showing you have no criminal record",["A traffic fine receipt","A school leaving certificate","A hostel pass"],"Some countries ask for police or character certificates with study visas."),
("If an agent says they can 'guarantee' your visa, what should you think?","Be careful – no one can guarantee a visa",["Pay them immediately","It must be true","Skip the official website"],"Only the government decides visas; guarantees are a common sign of fraud."),
("What does a 'scholarship letter' help prove?","That some or all of your costs are paid",["Your English level","Your age","Your nationality"],"Scholarships count as financial support in most visa applications."),
("Why is it important that your name is spelled the same on all documents?","Mismatches can delay or refuse your visa",["It looks nicer","It changes your fees","It is not important"],"Officers compare passport, admission and visa forms; differences cause problems."),
])
# Stage 2 – USA, UK, Canada
S.append([
("What is the main student visa for academic study in the USA?","F-1 visa",["H-1B visa","B-2 visa","L-1 visa"],"F-1 is for academic study; M-1 is for vocational courses and J-1 for exchanges."),
("Which form does a US school issue to an F-1 student?","Form I-20",["Form DS-2019","Form I-94","Form W-2"],"The I-20 is the Certificate of Eligibility for Nonimmigrant Student Status."),
("What is the DS-160?","The online US nonimmigrant visa application form",["A US bank form","A university exam","A tax form"],"You fill in the DS-160 online before booking your visa interview."),
("How much is the SEVIS I-901 fee for most F-1 students in 2026?","US$350",["US$185","US$50","US$1,000"],"The SEVIS fee is paid at fmjfee.com and the receipt is taken to the interview."),
("How much is the US student visa (MRV) application fee in 2026?","US$185",["US$350","US$25","US$500"],"Together with the SEVIS fee, government fees for an F-1 total about US$535."),
("In the UK, what is the CAS?","Confirmation of Acceptance for Studies",["Certificate of Academic Skills","Central Admission System","Card for Air Services"],"Your licensed UK sponsor gives you a CAS number to use in your visa application."),
("How many points does a UK Student visa applicant need?","70",["50","100","35"],"50 points for the CAS, 10 for money and 10 for English."),
("For a UK Student visa, money must be held for how many days in a row?","28 days",["7 days","90 days","365 days"],"The 28-day period must end within 31 days of the visa application date."),
("What is the UK monthly living-cost amount for students studying in London?","£1,529",["£1,171","£800","£2,500"],"Outside London the amount is £1,171 per month, counted for up to 9 months."),
("Up to how many months of living costs must UK Student visa applicants show?","9 months",["3 months","12 months","24 months"],"The UK counts maintenance for up to 9 months, whatever the course length."),
("How early can you apply for a UK Student visa from outside the UK?","Up to 6 months before the course",["Up to 2 years before","Only after arriving","Exactly 1 week before"],"GOV.UK lets you apply up to six months before your course start date."),
("What extra health payment do most UK visa applicants make?","Immigration Health Surcharge (IHS)",["National Health Card","Hospital Deposit Fee","Medical Bond"],"The IHS gives access to the UK's National Health Service during your stay."),
("What is the usual English level needed for UK degree-level study visas?","B2 on the CEFR scale",["A1","C2 only","No English needed"],"B2 is upper-intermediate; universities may set higher scores."),
("In Canada, what is a DLI?","Designated Learning Institution",["Direct Loan Interest","Digital Learning ID","Degree Level Index"],"Only DLIs can host international students on a study permit."),
("Which Canadian department issues study permits?","IRCC",["CRA","RCMP","CBC"],"Immigration, Refugees and Citizenship Canada handles study permits."),
("What letter do most Canadian study permit applicants need from the province?","Provincial or Territorial Attestation Letter (PAL/TAL)",["Provincial Tax Letter","Police Letter","Parent Approval Letter"],"Provinces issue PALs within the national study permit cap."),
("From 1 January 2026, who no longer needs a PAL in Canada?","Master's and PhD students at public institutions",["All undergraduates","All college students","Everyone from India"],"This exemption started on 1 January 2026 for graduate students at public DLIs."),
("Students going to Quebec need which extra certificate?","CAQ – Quebec Acceptance Certificate",["CAS","CoE","I-20"],"Quebec selects its own international students through the CAQ."),
("From 1 September 2026, how much must a single applicant outside Quebec show for living costs?","CAD 23,448",["CAD 10,000","CAD 15,000","CAD 50,000"],"This is in addition to first-year tuition and travel costs."),
("Where is a Canadian study permit actually issued after approval?","At the port of entry in Canada",["At the university","At a bank","By email only"],"Approved students get a letter to show the border officer, who issues the permit."),
("Which countries need you to give biometrics for study visas?","Many countries, including the UK, Canada and Ireland",["None at all","Only the USA","Only Japan"],"Biometrics help confirm identity and are now very common."),
])
# Stage 3 – Australia, New Zealand, Ireland, Germany
S.append([
("What is Australia's main student visa called?","Subclass 500",["Subclass 485","Subclass 600","Subclass 189"],"Subclass 485 is the post-study Temporary Graduate visa, not the student visa."),
("What document proves enrolment for an Australian student visa?","eCoE – electronic Confirmation of Enrolment",["CAS","I-20","PAL"],"You cannot lodge a subclass 500 application without a valid CoE."),
("What is OSHC in Australia?","Overseas Student Health Cover",["Online Study Hours Card","Official Student Housing Certificate","Overseas School Hall Code"],"OSHC is compulsory health insurance for international students."),
("Where do you apply online for an Australian student visa?","ImmiAccount",["UCAS","Common App","SOLAR"],"ImmiAccount is the Department of Home Affairs online system."),
("What did Australia's student visa charge rise to on 1 July 2026?","AUD 2,500",["AUD 500","AUD 1,000","AUD 5,000"],"It rose from AUD 2,000, after rising from AUD 1,600 in 2025."),
("How many hours can student visa holders in Australia work during study periods?","48 hours per fortnight",["10 hours per week","No work allowed","Unlimited hours"],"Work is limited during study periods so that study stays the main purpose."),
("Courses for Australian student visas must be on which register?","CRICOS",["ILEP","SEVIS","IND"],"CRICOS lists institutions and courses approved for overseas students."),
("What is the main New Zealand visa for international students paying fees?","Fee Paying Student Visa",["Working Holiday Visa","Visitor Visa","Skilled Migrant Visa"],"It can be granted for up to 4 years."),
("How much must a New Zealand student show for a year of living costs?","NZD 20,000",["NZD 5,000","NZD 50,000","NZD 1,000"],"For courses under a year, it is NZD 1,667 per month."),
("How many hours a week can most student visa holders in New Zealand work during study (since Nov 2025)?","25 hours",["10 hours","40 hours","None"],"The limit rose from 20 to 25 hours on 3 November 2025."),
("For Ireland, courses for non-EU students must be on which list?","ILEP – Interim List of Eligible Programmes",["CRICOS","SEVIS","PAL"],"Only courses on the ILEP qualify for student permission in Ireland."),
("Which online system is used to apply for an Irish study visa?","AVATS",["ImmiAccount","DS-160","SOLAR"],"AVATS is Ireland's online visa application system."),
("How much must students show for a course longer than 8 months in Ireland?","€10,000",["€2,000","€25,000","€500"],"This applies to both visa-required and non-visa-required students since 30 June 2025."),
("Which student immigration stamp do students register for in Ireland?","Stamp 2",["Stamp 4","Stamp 0","Stamp 6"],"Stamp 2 allows part-time work: 20 hours in term and 40 in holidays."),
("What is a German 'Sperrkonto'?","A blocked bank account for proof of funds",["A student ID card","A train pass","A health insurance plan"],"You can only withdraw a fixed amount each month from a blocked account."),
("How much must be in a German blocked account for one year in 2026?","€11,904",["€5,000","€20,000","€992"],"It is released at €992 per month."),
("What must you do soon after arriving in Germany?","Register your address (Anmeldung)",["Buy a car","Open a shop","Change your name"],"Address registration is needed before you get your residence permit."),
("Which certificate do Indian students usually need before a German student visa?","APS certificate",["CAS","I-20","CAQ"],"The Academic Evaluation Centre (APS) checks the authenticity of academic documents."),
("How many full days a year can students work in Germany?","140 full days (or 280 half days)",["30 days","365 days","No work allowed"],"Students can also take jobs at the university under separate rules."),
("Why is Germany popular despite needing a blocked account?","Many public universities charge little or no tuition",["No visa is needed","Classes are only online","It has no winter"],"Most German public universities charge only a small semester contribution."),
("What must the duration of OSHC in Australia cover?","Your whole visa period",["Only the first month","Only exam time","Only holidays"],"Keeping valid OSHC is a condition of the student visa."),
])
# Stage 4 – France, Netherlands, Japan, Singapore, Korea
S.append([
("What is the French long-stay student visa called?","VLS-TS 'étudiant'",["Schengen tourist visa","F-1","Subclass 500"],"VLS-TS means a long-stay visa equivalent to a residence permit."),
("Which organisation runs the 'Études en France' procedure?","Campus France",["UCAS","IRCC","ICA"],"Students from many countries, including India, must complete it before the visa."),
("From 1 August 2026, what monthly resources must French student visa applicants show?","€877.50",["€615","€300","€2,000"],"It rose from €615 and is now linked to the French minimum wage (SMIC)."),
("Within how long must you validate your French VLS-TS after arrival?","3 months",["1 day","1 year","No validation needed"],"Validation is done online and makes the visa work as a residence permit."),
("How many hours a year can students work in France?","964 hours",["100 hours","2,000 hours","No work allowed"],"964 hours equals about 60% of a full-time working year."),
("In the Netherlands, who submits the study residence permit application?","The university, on the student's behalf",["The student alone","The airline","The bank"],"Dutch law does not allow students to apply for a study permit themselves."),
("What is the Dutch 'MVV'?","A provisional residence permit/entry visa",["A student loan","A train ticket","A university exam"],"Some nationalities need an MVV to enter, plus the residence permit (VVR)."),
("Which Dutch agency decides residence permits?","IND",["DUO","KLM","UWV"],"The Immigration and Naturalisation Service (IND) handles visas and permits."),
("What share of credits must non-EU students in the Netherlands usually earn each year?","At least 50% of the ECTS",["10%","100%","None"],"Insufficient study progress can lead to the permit being withdrawn."),
("What does a Japanese school apply for on your behalf before your visa?","Certificate of Eligibility (CoE)",["I-20","CAS","IPA"],"The CoE is issued by Japan's Immigration Services Agency."),
("What card do students receive at the airport when entering Japan for study?","Residence Card",["Green Card","Aadhaar Card","Boarding Card"],"The Residence Card shows your status of residence in Japan."),
("What do students in Japan need before doing part-time work?","Permission to Engage in Activity Other Than That Permitted",["A driving licence","A second passport","Nothing at all"],"Working without this permission can risk your student status."),
("Which agency issues the Singapore Student's Pass?","ICA",["MOM","NEA","IRAS"],"The Immigration & Checkpoints Authority handles Student's Pass applications."),
("What is SOLAR in Singapore?","ICA's Student's Pass online system",["A solar power scheme","A train line","A scholarship"],"Students submit eForm 16 through SOLAR after the school registers them."),
("What letter do successful Student's Pass applicants receive first?","In-Principle Approval (IPA) letter",["CAS","CoE","I-20"],"The IPA is not the pass itself – formalities are completed after arrival."),
("How early can a new student arrive in Singapore before the course starts?","No more than 1 month before",["2 years before","Any time","Only after the course starts"],"ICA asks students to arrive close to the start date and present the IPA."),
("What is South Korea's main degree student visa?","D-2",["D-4","E-9","F-6"],"D-4 is used for language training; D-2 for degree programmes."),
("What document does a Korean university issue for the D-2 visa?","Certificate of Admission (CoA)",["CAS","I-20","PAL"],"The embassy uses the CoA to process your D-2 visa."),
("What card must students in Korea register for after arrival?","Alien Registration Card (ARC)",["Residence Card","Green Card","Stamp 2"],"The ARC is the identity card for foreign residents in Korea."),
("What happens to a D-2 visa if a student withdraws from university?","It ends and the student must leave",["It turns into a work visa","Nothing changes","It becomes permanent"],"Student visas depend on staying enrolled and studying."),
("Which country's student visa is called 'Student's Pass'?","Singapore",["Japan","France","Ireland"],"Singapore uses passes issued by ICA rather than a traditional visa label."),
])
# Stage 5 – mixed advanced
S.append([
("Which country's student visa uses a points system needing 70 points?","United Kingdom",["Germany","Japan","Singapore"],"UK points: CAS 50, finances 10, English 10."),
("Match: CoE is to Australia as CAS is to…","United Kingdom",["Canada","USA","France"],"Both are enrolment documents from the school used in the visa application."),
("Match: I-20 is to the USA as CoA is to…","South Korea",["Japan","Ireland","Germany"],"Each is the school-issued document needed for the student visa."),
("Which country requires a blocked account of €11,904 a year?","Germany",["France","Ireland","Netherlands"],"France uses a monthly resources rule; Ireland asks for €10,000."),
("In which country must the university, not the student, apply for the study permit?","Netherlands",["USA","UK","Canada"],"Dutch universities act as sponsors and apply to the IND."),
("Which country asks students to complete Études en France first?","France",["Belgium","Canada","Germany"],"It is managed by Campus France in many countries."),
("Which country has an annual national cap on study permits shared by provinces?","Canada",["UK","USA","Ireland"],"Provinces issue attestation letters within their share of the cap."),
("What is the UK 'Immigration Health Surcharge' for?","Access to the NHS during your stay",["Visa interview cost","University library","Airport tax"],"Most applicants pay the IHS as part of their visa application."),
("Which test checks if Australian applicants really intend to study?","Genuine Student (GS) requirement",["SEVIS check","ATAS check","APS check"],"It replaced the older GTE requirement in 2024."),
("What is ATAS in the UK?","A security clearance for certain sensitive subjects",["An English test","A tax form","A student loan"],"The Academic Technology Approval Scheme applies to some science and technology courses."),
("A UK applicant had £10,000 for 27 days, then 1 day at £9,000. Do they meet the 28-day rule?","No – the full amount must stay for 28 days in a row",["Yes, 27 days is enough","Yes, if they explain","Only in London"],"Any day below the required amount breaks the 28-day period."),
("Which country's living-cost requirement for students is NZD 20,000 per year?","New Zealand",["Australia","Singapore","Canada"],"Australia's figure is AUD 29,710 a year."),
("Which country gives students 48 hours of work per fortnight?","Australia",["New Zealand","Ireland","Germany"],"That is the same as an average of 24 hours a week."),
("Which country allows students 964 hours of work a year?","France",["Germany","Netherlands","Japan"],"Germany instead counts 140 full or 280 half days."),
("What should you do if a visa rule on a blog differs from the official website?","Follow the official website",["Follow the blog","Follow whichever is cheaper","Ignore both"],"Blogs can be out of date; official sites are updated when rules change."),
("Why do officers check the SOURCE of money, not just the balance?","To make sure funds are genuine and will stay available",["To charge extra tax","To choose your course","To pick your city"],"Sudden unexplained deposits are a common red flag in visa checks."),
("What is a 'visa refusal letter' useful for later?","Understanding the reasons so you can fix them before reapplying",["Nothing, throw it away","Getting a discount","Entering another country"],"Many countries also ask you to declare past refusals honestly."),
("Which document proves you can pay future years' fees in a multi-year course?","A credible funding plan, such as loans, savings or sponsorship",["A tourist visa","A photo album","A hotel booking"],"New Zealand, for example, says a credible plan for later years strengthens your application."),
("Which student permission in Ireland allows 40 hours a week of work?","Stamp 2 during holiday periods",["Stamp 2 during exams","Stamp 0 always","Tourist visa"],"During term, the limit is 20 hours a week."),
("What does 'maintaining status' usually require of international students?","Staying enrolled full-time and following work limits",["Travelling every month","Changing course often","Working full-time in term"],"Breaking study or work conditions can lead to losing your visa."),
("What is the best way to stay safe from visa fraud?","Apply only through official websites and authorised centres",["Pay cash to strangers","Share your passport online","Use agents who promise guarantees"],"Official portals and authorised visa centres are listed on government websites."),
])
rows=[];k=0
for li,st in enumerate(S,1):
    assert len(st)==21,(li,len(st))
    for qi,(q,a,w,e) in enumerate(st,1):
        pos=k%4;k+=1;opts=w[:];opts.insert(pos,a)
        rows.append([42,'Student Visas & Study Abroad',li,qi,q,*opts,'ABCD'[pos],e])
with open('../in/s42_L01-05.csv','w',newline='',encoding='utf-8') as f:
    wr=csv.writer(f,quoting=csv.QUOTE_NONNUMERIC);wr.writerow(['subject_id','subject','level','qno','question','option_a','option_b','option_c','option_d','correct','explanation']);wr.writerows(rows)
print(len(rows))
