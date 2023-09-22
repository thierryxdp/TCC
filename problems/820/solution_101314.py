def posLetra(string,letra,n):
    contagem=0
    m=string
    o=string
    if str.count(string,letra)<n:
        return -1
    while contagem<n: 
        x=str.index(m,letra)
        m=m[x+1:]
        contagem+=1
        return len(o)-len(m)-1