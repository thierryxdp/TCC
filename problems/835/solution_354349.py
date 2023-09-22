def melhor_volta(matriz):
    '''função que retorna qual foi o melhor tempo a cada volta na pista de Kart'''
    lista = []
    for x in range (0,6):
        lista.append(min(matriz[x]))
    melhor_tempo = min(lista)
    melhor_corr= lista.index(melhor_tempo)
    volta= matriz[melhor_corr].index(melhor_tempo)
    tupla = (melhor_corr+1,melhor_tempo,volta+1)
    return tupla