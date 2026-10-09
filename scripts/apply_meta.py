import json,glob,os,sys
sys.path.insert(0,os.path.dirname(__file__))
from meta import META
D=os.path.join(os.path.dirname(__file__),'..','src','data','tests')
cur={}
for f in glob.glob(D+'/*.json'):
    d=json.load(open(f,encoding='utf8')); cur[d['id']]=(f,d)
colors={}
for tid,slug,title,desc,group in META:
    f,d=cur[tid]
    d.update(slug=slug,title=title,desc=desc,group=group)
    new=os.path.join(D,'%02d-%s.json'%(tid,slug))
    json.dump(d,open(new,'w',encoding='utf8'),ensure_ascii=False,indent=1)
    if new!=f: os.remove(f)
print(len(META),'ok')
