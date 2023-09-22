def melhor_volta(matriz):
    '''
        recebe uma matriz contendo em cada coluna os dez tempos diferente que um
        corredor de carte fez em cada volta e cada linha contem os dados de um
        determinado corredor. retorna uma tupla contendo o corredor que fez a
        volta de menor tempo, o tenpo dessa volta e qual a ordem dessa volta
        entrada: lista
        saida: tupla
    '''
    corredor_rapido = ''
    tempo_rapido = 0.00
    volta_rapida = 0
    tempo_volta = []
    corredores = []
    resultado = ()
    indice = ''
    for i in range(len(matriz)):
        corredores = corredores + [(i + 1)]
        for j in range(len(matriz[0])):
            tempo_volta = tempo_volta + [matriz[i][j]]
    tempo_rapido = min(tempo_volta)
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if tempo_rapido in matriz[i]:
                corredor_rapido = corredores[i]
                volta_rapida = list.index(matriz[i], tempo_rapido) + 1
    resultado = (corredor_rapido, tempo_rapido, volta_rapida)
    return resultado