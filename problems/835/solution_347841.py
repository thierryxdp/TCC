def melhor_volta(matriz):
    lista=[]
    for i in matriz:
        for k in i:
            lista.append(k)
            melhor=min(lista)
            if melhor in i:
                return (matriz.index(i),melhor,i.index(melhor))