def melhor_volta(matriz_corrida):
    '''Função que recebe uma matriz 6 x 10, a qual cada termo corresponde
    ao tempo de volta de cada um dos 6 corredores de uma corrida em cada uma
    das 10 voltas. A função retornará em uma tupla o número do corredor, que
    obteve a melhor volta, qual o devido tempo e em qual volta 
    obteve o melhor tempo.
    [list] -> (tuple)'''
    n_linhas = len(matriz_corrida)
    lista_tempos_minimos = []
    for i in range(n_linhas):
        list.append(lista_tempos_minimos, min(matriz_corrida[i])
    
    menor_tempo = min(lista_tempos_minimos)
    corredor_melhor_tempo = list.index(lista_tempos_minimos, menor_tempo) + 1
    volta_melhor_tempo = list.index(matriz_corrida[corredor_melhor_tempo - 1], menor_tempo) + 1
    
    return corredor_melhor_volta, menor_tempo, volta_melhor_tempo