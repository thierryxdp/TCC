def melhor_volta(A):
    menor_tempo = None

    for (n_volta, tempos_voltas) in enumerate(A): 
        min_tempo = min(tempos_voltas)
        if (menor_tempo is None) or (min_tempo < menor_tempo):
            menor_tempo = min_tempo
            melhor_corredor = tempos_voltas.index(min_tempo) + 1
            melhor_volta = n_volta + 1
    return melhor_corredor, melhor_volta, menor_tempo