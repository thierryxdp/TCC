def posLetra(string,letra,n):
    s1=[]
    s2=''
    i=0
    while letra in string:
        s1.append(string[string.index(letra)])
        string.del(string.index(letra)])
    return s1[n]