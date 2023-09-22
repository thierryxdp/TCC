def posLetra(frase,letra,vezes):
    t=len(frase)
    p=str.index(frase,letra)
    q=str.count(frase,letra)
    i=0
    a=0
    if p==vezes:
        return p
    elif q<vezes:
        return -1
    
    while i<t:
        i=i+1
        a=a+1
    return frase[p]