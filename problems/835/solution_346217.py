def melhor_volta(matriz):
    lista2=[]
    for i in range(len(matriz)):
        lista=list.sort(matriz[i])
        lista2+=[lista[i][0]]
        melhor=min(lista2)
        return (i,melhor)