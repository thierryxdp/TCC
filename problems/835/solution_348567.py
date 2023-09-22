def melhor_volta(matriz):
    
    k = 0
    for lin in matriz:
        k = min(lin)
        lista.append(k)
    
    tempo = min(lista)
    corredor = lista.index(tempo)
    num_volta = matriz[corredor].index(tempo)
    
    return (corredor + 1, tempo, num_volta + 1)