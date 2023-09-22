def melhor_volta(matriz):
    tempo = 99999999999
    melhorvolta = []
    tempo = 0
    for a, b in enumerate(matriz):
        for c, d in enumerate(matriz[a]):
            if d < tempo:
                tempo = d
                melhorvolta = [a, c]
    return (melhorvolta[0], tempo, melhorvolta[1])