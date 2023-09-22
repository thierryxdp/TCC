def melhor_volta(matriz):
    tempo = 99999999999
    melhorvolta = []
    for a, b in enumerate(matriz):
        for c, d in enumerate(matriz[a]):
            if d < tempo:
                tempo = d
                melhorvolta = [a + 1, c + 1]
    return (melhorvolta[0], tempo, melhorvolta[1])