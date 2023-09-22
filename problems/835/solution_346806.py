def melhor_volta(voltas):
    """ """
    menor_tempo = min(voltas[0])
    corredor_rapido = 0
    
    for corredor in range(len(voltas)):
        if menor_tempo > min(voltas[corredor]):
            menor_tempo = min(voltas[corredor])
            volta = list.index(voltas[corredor],menor_tempo)
            corredor_rapido = corredor
    return(corredor_rapido, menor_tempo, volta)