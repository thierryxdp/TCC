def faltante(x):
    k=[]
    for i in range(len(x)):
       if x[i]==i+1:
           k.append(i+1)
           if k==x:
               k.append(x[-1]+1)
       else:
           k.append(i+1)
    return k[-1]