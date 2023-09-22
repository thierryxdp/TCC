def faltante(l):
    'retorna o numero que falta na lista..int---int'
    x=0
    n=1
    faltante=len(l)+1
    while x<len(l):
        if l[x]!=n:
            faltante=n
            break
        n +=1
        x+=1
    return faltante