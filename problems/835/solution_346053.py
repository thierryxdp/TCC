def melhor_volta(matriz):
    melhor = ()
    menor = []
    for i in matriz:
        x = min(i)
        list.append(menor,x)
    y = min(menor)
    for i in matriz:
        if y in i:
            melhor = (matriz.index(i),y)
    return melhor