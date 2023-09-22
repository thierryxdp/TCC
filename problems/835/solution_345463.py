def melhor_volta(matriz):
    menores=[]
    onde=[]
    p=[]
    for c in range(len(matriz)):
        n=min(matriz[c])
        for i in range(len(matriz[c])):
            if matriz[c][i]==n:
                menores=menores+[matriz[c][i]]
                onde=onde+[i]
                p=p+[c+1]
    menor=min(menores)
    loc=onde[menores.index(menor)]+1
    quem=p[menores.index(menor)]
    return (quem,menor,loc)