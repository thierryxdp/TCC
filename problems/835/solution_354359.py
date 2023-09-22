def melhor_volta(matriz):
    """ Dado uma matriz contendo os resultados de 6 competidores em suas voltas, retorna uma tupla contendo de quem foi a melhor  volta, o tempo e qual volta.
    entrada matriz -> saida tupla. """
    
    competidor = 0
    tempo = 100000
    volta = 0
    tupla = ()
    
    for i in range(len(matriz)):
        if tempo > min(matriz[i]):
            tempo = min(matriz[i])
            competidor = i+1
            for j in range(len(matriz[i])):
                if matriz[i][j] == tempo:
                    volta = matriz[i][j]
    tupla = (competidor, tempo, volta)
    return tupla