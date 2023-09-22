def melhor_volta(matriz):
    '''funcao que dado uma matriz 6x10 como entrada com os tempos em segundos dos corredores em cada volta, retorna uma tupla informando de quem foi a melhor volta da prova, qual foi o tempo e qual foi o numero da volta
    matriz->tupla'''
    melhortempo=[]
    for i in range(len(matriz)):
        menortempo=min(matriz[i])
        list.append(melhortempo,menortempo)
    mintempo=min(melhortempo)
    piloto=melhortempo.index(mintempo)
    volta=matriz[piloto].index(mintempo)
    return (piloto, mintempo, volta)