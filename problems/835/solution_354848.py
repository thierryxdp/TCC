def melhor_volta(matriz):
    lista_tempos = []  
    lista_voltas = []
    for voltas in range(6):  
        for tempos in range(10):  
            if matriz[voltas][tempos] == min(matriz[voltas]):  
                lista_tempos.append(tempos)  
    for i in range(6):
      lista_voltas.append(matriz[i][lista_tempos[i]])