def busca_piloto(x,y):
    for k in range(len(y)):
        if y[k][0] == x[1]:
            return k

def melhor_volta(matriz):
    melhor=[]
    for k in matriz:
        minimo = min(k)
        min_index=[]
        for i in range(0,len(k)):
            if minimo == k[i]:
                min_index.append(i)
                melhor.append([round(minimo,2),min_index[0]])

    tempo, volta = min(melhor)[0], min(melhor)[1]
    piloto = busca_piloto((0,tempo,volta),melhor)
    return (piloto,tempo,volta)