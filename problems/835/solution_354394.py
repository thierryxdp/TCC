def melhor_volta(matriz):
    """Retorna uma tupla informando de quem foi
    a melhor volta da prova, com qual tempo e
    em que volta, dado uma matriz 6x10 onde as 
    linhas sao os corredores e as colunas sao
    as voltas de uma corrida.
    list -> tup"""
    tempo = matriz[0].index(min(matriz[0]))
    for i in range(0, len(matriz)):
        for j in range(0, len(matriz[i])):
            if min(matriz[i][j], tempo) == matriz[i][j]:
                tempo = min(matriz[i][j],tempo)
                vencedor = i + 1
                volta = j + 1
    return vencedor, tempo, volta