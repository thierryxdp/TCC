def melhor_volta(matriz):
    '''Funcao que recebe uma matriz com os tempos contendo
6 linhas - representando os corredores - e 10
colunas - representando as voltas - retornando uma
tupla informando de quem foi a melhor volta, com quaal
tempo e em que volta'''
    volta = matriz[0][0]
    tupla = (1,volta,1)
    for linha in range(len(matriz)):
        novaVolta = min(matriz[linha])
        volta = min(volta,novaVolta)
        for coluna in range(len(matriz[0])):
            tempo = matriz[linha][coluna]
            if tempo == volta:
                tupla = (coluna+1,volta,linha+1)
    return tupla