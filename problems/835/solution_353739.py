def melhor_volta(matriz):
    '''
    Funcao que recebe uma matriz de 6x10 representando os tempos
    de 10 voltas para 6 corredores. A funcao retorna uma tupla
    informando de quem foi a melhor volta,com qual tempo e em que volta.
    list -> tuple
    '''
    menor_tempo_lista = []
    menor_volta_lista = []
    for i in range(len(matriz)):
        valor_minimo = min(matriz[i])
        menor_tempo_lista.append(valor_minimo)
        menor_volta_lista.append(matriz[i].index(valor_minimo))
                                
    menor_tempo_corredor = min(menor_tempo_lista)
    corredor = menor_tempo_lista.index(menor_tempo_corredor) + 1
    index_menor_volta = menor_tempo_lista.index(menor_tempo_corredor)                                           
    volta_menor_tempo = menor_volta_lista[index_menor_volta] + 1
    
    return (corredor, menor_tempo_corredor, volta_menor_tempo)