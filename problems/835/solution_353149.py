def melhor_volta(matriz):
    '''retorna a volta mais rapida da corrida
    list(list) -> int'''
    tempos = []
    for i in range(len(matriz)):
        menorcorredor = min(matriz[i])
        for j in range(len(matriz[i])):
            tempos += matriz[i][j]
            menor = min(tempos)
            if menorcorredor <= menor:
                corredor = i
                return i , menor, list.index(menor)