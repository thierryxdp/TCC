def melhor_volta(mat):

    menor_tempo = mat[0][0]
    corredor_rapido = 1
    volta = 1

    for corredor, tempos in enumerate(mat):
        for v, tempo in enumerate(tempos, start=1):
            if tempo < menor_tempo:
                menor_tempo = tempo
                corredor_rapido = corredor+1
                volta = v+1

    return (corredor_rapido, menor_tempo, volta)