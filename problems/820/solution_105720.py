def posLetra(string,letra,n):
    s1=[]
    s2=[string]
    i=0
    while letra in string:
        s1.append(string[string.index(letra)])
        del s2[string.index(letra)]
    return s1[n]