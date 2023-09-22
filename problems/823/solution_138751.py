def faltante(x):
    k=[]
    l=[]
    for i in range(len(x)):
       if x[i]==i+1:
           l.append(i)
       else:
           k.append(i+1)
    return int(k)