def melhor_volta(voltas):
    """ """
    menor_tempo = min(voltas[0])
    corredor_rapido = 0
    volta = 0
    
    for corredor in range(len(voltas)):
        if menor_tempo >= min(voltas[corredor]):
            menor_tempo = min(voltas[corredor])
            volta = list.index(voltas[corredor],menor_tempo)
            corredor_rapido = corredor
    return(corredor_rapido+1, menor_tempo, volta+1)