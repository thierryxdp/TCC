def repetidos(L):
    ft=L[1:]
    r=[]
    for i in range(len(ft)):
        if L[i]==ft[i]:
            r+=r=1
    return r