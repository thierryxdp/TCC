def qtd_divisores(x):
    k=1
    l=[]
    while k<=x:
        if x%k==0:
            l.append(k)
        k+=1
    return len(l)