def uppCons(a:str) -> str:
    b=[]
    i=0
    while i<len(a):
        if a[i] == 'a' and 'e' and 'i' and 'o' and 'u':
            b.append(a[i])
        else:
            b.append(a.upper())
        return b