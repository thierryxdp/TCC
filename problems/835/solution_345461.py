def melhor_volta(matriz):
    for c in range(len(matriz)):
        n=min(matriz[c])
        menores=[]
        onde=[]
        for i in range(len(matriz[c])):
            if matriz[c][i]==n:
                menores=menores+matriz[c][i]
                onde=onde+i
        menor=min(menores)
        loc=onde[menores.find(menor)]
    return (menor,loc)