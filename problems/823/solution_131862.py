def faltante(x):
    y=[0]+x+[0]
    t=0
    h=list(range(len(x)+1))+[x]+[0]
    while t<=len(y):
        if h[t]!=y[t]:
            return y[a-1]+1
        a+=1