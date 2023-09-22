def melhor_volta(matriz):
    tempo = 100000
    melhor_volta = 0
    corredor = 0
    indice = 1
    for i in matriz:
        if min(i) < tempo:
            tempo = min(i)
            corredor = indice
            melhor_volta = i.index(tempo) + 1
        indice +=1
    return (corredor, tempo, melhor_volta)