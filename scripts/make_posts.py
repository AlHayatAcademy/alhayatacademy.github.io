# One-off generator for src/data/posts.json (after generation, edit the JSON directly).
import json,os
GA_ALL=["Current Affairs","GK & Geography","Pakistan Studies","Islamic Studies","Maths & Reasoning","English","Urdu","Everyday Science","Computer & IT"]
def ga(label="General Ability",weight=None,note="",groups=None,covered=True):
    return {"label":label,"weight":weight,"groups":groups or GA_ALL,"covered":covered,"note":note}
def own(label,weight,note):
    return {"label":label,"weight":weight,"groups":[],"covered":False,"note":note}
P=[]
P.append({"slug":"junior-clerk","name":"Junior Clerk","bps":"BS-11","dept":"Board of Revenue / District offices","icon":"🗂️","color":"#7c3aed","priority":1,
 "summary":"The most advertised PPSC post. One MCQ paper: 80% General Ability and about 20% MS Office and computer skills, followed by a typing and proficiency test.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[ga("General Ability",80,"General Knowledge, Pakistan Studies, Current Affairs, Islamic Studies (GK for non-Muslims), Geography, Basic Mathematics, English, Urdu and Everyday Science.",[g for g in GA_ALL if g!="Computer & IT"]),
             ga("MS Office and computer skills",20,"Questions on MS Office and computer skills.",["Computer & IT"])],
 "mix":{"Current Affairs":9,"GK & Geography":18,"Pakistan Studies":9,"Islamic Studies":8,"Maths & Reasoning":9,"English":9,"Urdu":9,"Everyday Science":9,"Computer & IT":20},
 "stages":["Written MCQ test (100 marks)","Only those who qualify the General Ability test are called for the English typing and proficiency test (shortlisting ratio 1:20 in several advertisements)"],
 "ads":[{"case":"25J2025","where":"Deputy Commissioner Office, Sahiwal (Board of Revenue)","posts":20,"basis":"Regular"},
        {"case":"26J2025","where":"DC / District Collector Office, Sheikhupura (Board of Revenue)","posts":19,"basis":"Regular"},
        {"case":"33J2025","where":"Board of Revenue, Punjab","posts":25,"basis":"Regular"},
        {"case":"28J2026","where":"Bahawalpur Division (Board of Revenue)","posts":8,"basis":"Contract, 3 years"},
        {"case":"30J2026","where":"Deputy Commissioner Office, Kot Addu (Board of Revenue)","posts":10,"basis":"Contract, 3 years"},
        {"case":"32J2026","where":"Additional Deputy Commissioner (Revenue), Kot Addu","posts":2,"basis":"Contract, 3 years"},
        {"case":"37J2026","where":"DC / District Collector Office, Faisalabad (Board of Revenue)","posts":19,"basis":"Contract, 3 years"}],
 "faq_extra":[("Is there a typing test for Junior Clerk?","Yes. The syllabi say only candidates who qualify the written General Ability test are called for the English typing and proficiency test. Practise typing on a computer alongside MCQs.")]})
P.append({"slug":"assistant","name":"Assistant","bps":"BS-16","dept":"Deputy Commissioner offices / Board of Revenue","icon":"📁","color":"#0ea5e9","priority":2,
 "summary":"A single General Ability MCQ paper that includes Basic Computer Studies. No fixed subject split is printed, so all subjects matter.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[ga("General Ability",100,"General Knowledge, Pakistan Studies, Current Affairs, Islamic Studies (GK for non-Muslims), Geography, Basic Mathematics, English, Urdu, Everyday Science and Basic Computer Studies.")],
 "mix":{"Current Affairs":10,"GK & Geography":20,"Pakistan Studies":10,"Islamic Studies":9,"Maths & Reasoning":10,"English":10,"Urdu":10,"Everyday Science":10,"Computer & IT":11},
 "stages":["Written MCQ test (100 marks)"],
 "ads":[{"case":"29J2026","where":"Deputy Commissioner Office, Kot Addu","posts":1,"basis":"Contract, 3 years"},
        {"case":"36J2026","where":"DC / District Collector Office, Faisalabad (Board of Revenue)","posts":5,"basis":"Contract, 3 years"}],"faq_extra":[]})
P.append({"slug":"deputy-accountant","name":"Deputy Accountant","bps":"BS-16","dept":"Punjab Treasuries & Accounts Service (Finance Department)","icon":"🧾","color":"#16a34a","priority":3,
 "summary":"A big recruitment (60 posts in the latest advertisement) with a pure General Ability paper, so the same preparation as Assistant applies.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[ga("General Ability",100,"General Knowledge, Pakistan Studies, Current Affairs, Islamic Studies (GK for non-Muslims), Geography, Basic Mathematics, English, Urdu, Everyday Science and Basic Computer Studies.")],
 "mix":{"Current Affairs":10,"GK & Geography":20,"Pakistan Studies":10,"Islamic Studies":9,"Maths & Reasoning":10,"English":10,"Urdu":10,"Everyday Science":10,"Computer & IT":11},
 "stages":["Written MCQ test (100 marks)"],
 "ads":[{"case":"4A2026","where":"Punjab Treasuries & Accounts Service (Finance Department)","posts":60,"basis":"Regular"}],"faq_extra":[]})
P.append({"slug":"enforcement-officer","name":"Enforcement Officer","bps":"BS-17","dept":"Punjab Revenue Authority (Finance Department)","icon":"🏛️","color":"#f59e0b","priority":4,
 "summary":"The biggest single recruitment in the set (199 posts). Half the paper is Accounting, Finance and the Sales Tax Act 2012 (Sales Tax on Services); half is General Ability.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[own("Accounting, Finance and Sales Tax Act, 2012 (Sales Tax on Services)",50,"Subject questions. This site does not yet have a bank for this part."),
             ga("General Ability",50,"General Knowledge, Pakistan Studies, Current Affairs, Islamic Studies (GK for non-Muslims), Geography, Basic Mathematics, English, Urdu, Everyday Science and Basic Computer Studies.")],
 "mix":{"Current Affairs":5,"GK & Geography":10,"Pakistan Studies":5,"Islamic Studies":4,"Maths & Reasoning":5,"English":5,"Urdu":5,"Everyday Science":5,"Computer & IT":6},
 "stages":["Written MCQ test (100 marks)"],
 "ads":[{"case":"02-RA/2026 (Adv. 05/2026)","where":"Punjab Revenue Authority, Finance Department","posts":199,"basis":"Contract, 3 years, likely to be extended"}],"faq_extra":[]})
P.append({"slug":"junior-computer-operator","name":"Junior Computer Operator","bps":"BS-12","dept":"Additional Deputy Commissioner office, Kot Addu (BOR)","icon":"🖥️","color":"#4f46e5","priority":5,
 "summary":"100% MS Office and IT questions, followed by a typing and proficiency test for qualified candidates.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[ga("MS Office and I.T related questions",100,"The proportion of the MCQ test is MS Office and IT (100%).",["Computer & IT"])],
 "mix":{"Computer & IT":100},
 "stages":["Written MCQ test (100 marks)","Qualified candidates are called for typing and proficiency test at a ratio of 1:20"],
 "ads":[{"case":"34J2026","where":"Additional Deputy Commissioner Office, Kot Addu (BOR)","posts":2,"basis":"Contract, 3 years"}],"faq_extra":[]})
P.append({"slug":"stenographer","name":"Stenographer","bps":"BS-15","dept":"Deputy Commissioner offices (Board of Revenue)","icon":"⌨️","color":"#ef4444","priority":6,
 "summary":"Skills based: English shorthand and typing first, then a computer proficiency test, then Urdu shorthand and typing.",
 "pattern":"Shorthand and typing tests (no MCQ paper listed in the syllabi we reviewed)",
 "syllabus":[own("English shorthand",None,"70 words per minute in shorthand."),own("English typewriting",None,"35 words per minute."),own("Urdu shorthand and typing",None,"Shorthand at 60 wpm and typing at 25 wpm, for candidates who qualify the English tests.")],
 "mix":None,
 "stages":["English shorthand test","English typing and proficiency test on computer (ratio 1:20)","Urdu shorthand and typing (for those who qualify)"],
 "ads":[{"case":"31J2026","where":"Deputy Commissioner Office, Kot Addu (BOR)","posts":2,"basis":"Contract, 3 years"},
        {"case":"33J2026","where":"Additional Deputy Commissioner Office, Kot Addu (BOR)","posts":1,"basis":"Contract, 3 years"},
        {"case":"35J2026","where":"DC / District Collector Office, Faisalabad (BOR)","posts":17,"basis":"Contract, 3 years"}],"faq_extra":[]})
P.append({"slug":"public-relations-officer","name":"Public Relations Officer","bps":"BS-17","dept":"Punjab Food Authority (Price Control & Commodities Management Dept.)","icon":"📣","color":"#db2777","priority":7,
 "summary":"60% mass communication / media studies, 20% English and 20% Urdu, followed by an MS Office proficiency test.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[own("Mass Communication / Journalism / Media Studies / Media Management / Communication Studies",60,"Subject questions. Not yet available on this site."),
             ga("English Language",20,"English language questions.",["English"]),ga("Urdu Language",20,"Urdu language questions.",["Urdu"])],
 "mix":{"English":20,"Urdu":20},
 "stages":["Written MCQ test (100 marks)","MS Office proficiency test for qualified candidates (ratio 1:20)"],
 "ads":[{"case":"13J2026","where":"Punjab Food Authority","posts":1,"basis":"Contract, 3 years"}],"faq_extra":[]})
P.append({"slug":"market-committee-secretary","name":"Secretary Market Committee (A and B Class)","bps":"BS-16","dept":"Punjab Agricultural Marketing Regulatory Authority (PAMRA)","icon":"🌾","color":"#65a30d","priority":8,
 "summary":"60% qualification related questions and 40% General Ability, for both A-class and B-class market committees.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[own("Qualification related questions",60,"Subject questions according to the required qualification."),
             ga("General Ability",40,"General Knowledge, Pakistan Studies, Current Affairs, Geography, Everyday Science, Basic Mathematics, English, Urdu and Basic Computer Studies.",["Current Affairs","GK & Geography","Pakistan Studies","Everyday Science","Maths & Reasoning","English","Urdu","Computer & IT"])],
 "mix":{"Current Affairs":4,"GK & Geography":8,"Pakistan Studies":4,"Everyday Science":4,"Maths & Reasoning":5,"English":5,"Urdu":5,"Computer & IT":5},
 "stages":["Written MCQ test (100 marks)"],
 "ads":[{"case":"46J2026","where":"PAMRA, B-class Market Committees","posts":15,"basis":"Contract, 5 years"},{"case":"47J2026","where":"PAMRA, A-class Market Committees","posts":9,"basis":"Contract, 5 years"}],"faq_extra":[]})
P.append({"slug":"chief-officer-municipal-officer-regulations","name":"Chief Officer / Municipal Officer (Regulations)","bps":"BS-16 / BS-17","dept":"Local Government & Community Development Department","icon":"🏙️","color":"#0891b2","priority":9,
 "summary":"The service-quota advertisement tests the Punjab Local Government Act 2025 plus General Ability. The direct-recruitment advertisement lists only qualification related questions.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[own("The Punjab Local Government Act, 2025",None,"Service quota (BS-16, case 39J2026). The split between the Act and General Ability is not printed."),
             ga("General Ability",None,"General Knowledge, Pakistan Studies, English, Urdu, Basic Mathematics and Basic Computer Studies.",["GK & Geography","Pakistan Studies","English","Urdu","Maths & Reasoning","Computer & IT"])],
 "mix":{"GK & Geography":10,"Pakistan Studies":10,"English":10,"Urdu":8,"Maths & Reasoning":6,"Computer & IT":6},
 "stages":["Written MCQ test (100 marks)"],
 "ads":[{"case":"39J2026","where":"LG&CD Department, service quota (BS-16)","posts":30,"basis":"Service quota"},
        {"case":"23J2026","where":"LG&CD Department, direct recruitment (BS-17), qualification related questions only","posts":46,"basis":"Regular"}],"faq_extra":[]})
P.append({"slug":"deputy-director-environment","name":"Deputy Director (Environment, Climate Change, Strategy & Policy)","bps":"BS-18","dept":"Punjab Environment Protection and Climate Change Department","icon":"🌳","color":"#059669","priority":10,
 "summary":"50% General Ability and 50% environmental laws, rules and policies (a long list is printed in the syllabus).",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes",
 "syllabus":[ga("General Ability",50,"General Knowledge, Pakistan Studies, Current Affairs, Islamic Studies (GK for non-Muslims), Geography, Basic Mathematics, English, Urdu, Everyday Science and Basic Computer Studies."),
             own("Acts, laws, rules and regulations",50,"Punjab Environmental Protection (Amendment) Act 2017; Polythene Bags Ordinance 2002; Punjab Clean Air Policy; Policy on Controlling Smog 2017; National Climate Change Policy; Delegation of Powers Rules 2017; Hospital Waste Management Rules 2014; Motor Vehicles Rules 2013; NEQS Self-Monitoring Rules 2001.")],
 "mix":{"Current Affairs":5,"GK & Geography":10,"Pakistan Studies":5,"Islamic Studies":4,"Maths & Reasoning":5,"English":5,"Urdu":5,"Everyday Science":5,"Computer & IT":6},
 "stages":["Written MCQ test (100 marks)"],
 "ads":[{"case":"55G2025","where":"Deputy Director (Strategy & Policy)","posts":1,"basis":"Contract, 3 years"},{"case":"56G2025","where":"Deputy Director (Climate Change)","posts":1,"basis":"Contract, 3 years"}],"faq_extra":[]})
P.append({"slug":"child-protection-officer","name":"Child Protection Officer","bps":"BS-17","dept":"Child Protection & Welfare Bureau, Home Department","icon":"🛡️","color":"#9333ea","priority":11,
 "summary":"Preparation for the CPO test (Case No. 07-RB/2026). The official CPO syllabus was not in our collection, so two mock papers cover both likely patterns. Verify the syllabus on ppsc.gop.pk.",
 "pattern":"1 paper · MCQs · 100 marks · 90 minutes (as commonly reported)",
 "syllabus":[ga("General Ability (as seen in a comparable CPO paper)",None,"Current affairs, Pakistan Studies, English, Urdu, computer, maths and Islamic Studies.",GA_ALL),
             {"label":"Child protection subject area (possible)","weight":None,"groups":["Child Protection Act","Child Rights & Law","Social Sciences"],"covered":True,"note":"The Punjab Destitute and Neglected Children Act 2004, child rights, social work, psychology and criminology."}],
 "mix":{"Current Affairs":18,"GK & Geography":17,"Pakistan Studies":16,"English":13,"Urdu":11,"Everyday Science":5,"Computer & IT":5,"Maths & Reasoning":8,"Islamic Studies":7},
 "mix2":{"Child Protection Act":20,"Child Rights & Law":15,"Social Sciences":15,"Pakistan Studies":10,"Islamic Studies":5,"Current Affairs":10,"GK & Geography":5,"Everyday Science":2,"Computer & IT":3,"English":8,"Urdu":4,"Maths & Reasoning":3},
 "stages":["Written MCQ test"],"ads":[{"case":"07-RB/2026","where":"Child Protection & Welfare Bureau, Home Department","posts":26,"basis":"Contract, 3 years"}],"faq_extra":[]})
P.append({"slug":"general-ability","name":"General Ability (all PPSC posts)","bps":"All","dept":"Common to most PPSC MCQ tests","icon":"🎯","color":"#e11d48","priority":0,
 "summary":"The shared core of PPSC recruitment tests. Master this and you are ready for Junior Clerk, Assistant, Deputy Accountant and the general half of many other papers.",
 "pattern":"Typically 100 MCQs · 90 minutes",
 "syllabus":[ga("General Ability",100,"General Knowledge, Pakistan Studies, Current Affairs, Islamic Studies (GK for non-Muslims), Geography, Basic Mathematics, English, Urdu, Everyday Science and Basic Computer Studies.")],
 "mix":{"Current Affairs":10,"GK & Geography":20,"Pakistan Studies":10,"Islamic Studies":9,"Maths & Reasoning":10,"English":10,"Urdu":10,"Everyday Science":10,"Computer & IT":11},
 "stages":["Written MCQ test"],"ads":[],"faq_extra":[]})
P.sort(key=lambda p:p["priority"])
json.dump(P,open(os.path.join(os.path.dirname(__file__),"..","src","data","posts.json"),"w",encoding="utf8"),ensure_ascii=False,indent=1)
print(len(P))
