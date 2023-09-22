def repetidos(L):
    ft=L[1:]
    r=0
    for i in range(len(ft)):
        if L[i]==ft[i]:
            r+=1
    return r