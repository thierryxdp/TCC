def qtd_divisores(x):
    k=1
    l=[]
    while k<=x:
        if x%k==0:
            l.append(k)
    return len(l)