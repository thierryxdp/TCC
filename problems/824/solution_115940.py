def uppCons(a:str) -> str:
    b=[]
    i=0
    while indice<len(a):
        if a[indice] == 'a':
            b.append(a[i])
        else:
            b.append(a.upper())
        return b