def faltante(L):
    list.sort(L)
    y=1
    resp=0
    if L[0]!=1:
        return 1
    for x in L[:-1]:
        if L[y-1]==L[y]-1:
            y+=1
        else:
            resp=x+1
            break
    if resp==0:
        resp=L[-1]
    return resp