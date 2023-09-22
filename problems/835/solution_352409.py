def melhor_volta(matriz):
    melhor_volta=0
    tempo=100000
    corredor=0
    indice= 1 
    for i in matriz:
        if min(i) < tempo:
            tempo = min (i)
            corredor = indice
            indice += 1
            melhor_volta = i.index(tempo)+1
        return(corredor,tempo,melhor_volta)