import re
import requests as r
f=open('index.htm','r');t=f.read();f.close()
t=[a.split('"')[0]for a in t.split('data-original="')[1:]if'_r.jpg'in a.split('"')[0]]
t2=[]
for a in t:
    if a not in t2:t2.append(a)
t=t2
n=0
ll=len(t)
for a in t:
    n+=1
    print(n,'/',ll)
    d=r.get(a,stream=True,timeout=5)
    f=open('%s.jpg'%str(n).rjust(6).replace(' ','0'),'wb+');f.write(d.content);f.close()
