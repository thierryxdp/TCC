def melhor_volta(matriz):
    
    tempos = []
    for i in matriz:
        for j in i:
            tempos.append(j)
    
    tempo = min(tempos)
    contador = 0
    while tempo not in matriz[contador]:
        contador += 1
    corredor = contador + 1
    n_volta = matriz[contador].index(tempo) +1
    
    return corredor, tempo, n_volta