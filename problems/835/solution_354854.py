def melhor_volta(matriz):
    c=[]
    d=[]
    n=0
    while n<len(matriz):
        tempo=min(matriz[n])
        list.append(c,tempo)
        volta=list.index(matriz[n],tempo)
        list.append(d,volta)
    menor=list.index(min(c),c)
    return ((list.index(menor,c)+1),min(c),(d[menor]+1))