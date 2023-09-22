def melhor_volta(matriz):
    c=[]
    d=[]
    n=0
    while n<len(matriz):
        list.append(c,min(matriz[n]))
        volta=list.index(matriz[n],min(matriz[n]))
        list.append(d,volta)
    menor=c.index(min(c))
    return ((list.index(menor,c)+1),min(c),(d[menor]+1))