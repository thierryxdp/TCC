def melhor_volta(voltas):
    """A funcao recebe o placar de uma corrida com
       o tempo de cada corredor e compara os tempos e
       retorna respectivamente o Corredor mais rapido,
       o menor tempo, e em qual volta foi o menor tempo.

       list, -> tuple """
    menor_tempo = min(voltas[0])
    corredor_rapido = 0
    volta = 0
    
    for corredor in range(len(voltas)):
        if menor_tempo >= min(voltas[corredor]):
            menor_tempo = min(voltas[corredor])
            volta = list.index(voltas[corredor],menor_tempo)
            corredor_rapido = corredor
    return(corredor_rapido+1, menor_tempo, volta+1)