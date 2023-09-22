def melhor_volta(matriz):
    ''' funcao que apos dar como entrada uma matriz com um tempo dos corredores ira retornar uma tupla com o melhor corredor, melhor tempo e melhor volta
matris = tupla ''' 
    placar = []
    for i in matriz:
        list.append(placar, min(i))
        corredor = list.index(placar,min(placar))
    volta = list.index(matriz[corredor], min(placar))
    tupla = (corredor+1, min(placar), volta+1)
    return tupla