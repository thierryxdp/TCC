def melhor_volta(matriz):
    lista=[]
    for i in matriz:
        for k in i:
            lista.append(k)
            melhor=min(lista)
            if melhor in i:
                tupla=(matriz.index(i)+1,melhor,i.index(melhor)+1)
    return tupla