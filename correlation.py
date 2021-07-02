# Add the functions in this file
import json
def load_journal(x):
    
    f=open(x)
    l=json.load(f)
    f.close()
    return l

def compute_phi(fn,ev):
    jfile=load_journal(fn)
    x=[]
    y=[]
    n11=n00=n01=n10=0
    n1_=n_1=n0_=n_0=0
    for i in jfile:
        if ev in i['events']:
            x.append(True)
        else:
            x.append(False)
        y.append(i['squirrel'])
    
    for i in range(len(jfile)):
        if x[i] and y[i]:
            n11+=1
        if not x[i] and not y[i]:
            n00+=1
        
        if x[i] and not y[i]:
            n10+=1
        if not x[i] and y[i]:
            n01+=1
        if x[i]:
            n1_+=1
        if not x[i]:
            n0_+=1
        if y[i]:
            n_1+=1
        if not y[i]:
            n_0+=1
    #print(n11,n00,n01,n10,n1_,n_1,n0_,n_0)
    a=(n11*n00) - (n10*n01)
    b=(n1_*n0_*n_1*n_0)**(0.5)
    #print(a,b)
    return ((n11*n00) - (n10*n01))/(n1_*n0_*n_1*n_0)**(0.5)

def compute_correlations(fn):
    jfile=load_journal(fn)
    d={}
    for i in jfile:
        for j in i['events']:
            if j not in d:
                d[j]=compute_phi(fn,j)
    return d

def diagnose(fn):
    d=compute_correlations(fn)
    cal=d.values()
    for key,value in d.items():
        if value==max(cal):
            a=key
        if value==min(cal):
            b=key
    return a,b






