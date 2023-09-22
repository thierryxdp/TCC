def melhor_volta(tempos):

    menor_tempo = min(tempos[0])
    corredor = 0

    for e, el in enumerate(tempos, start=1):
        if min(e) < menor_tempo:
            corredor = e
            menor_tempo = min(e)

    return (corredor, menor_tempo)