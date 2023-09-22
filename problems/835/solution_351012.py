def melhor_volta(matriz):
    lista_pelos_tempos = []  
    lista_pelas_voltas = [] 
    
    for voltas in range(6):  
        for tempos in range(10):  
            if matriz[voltas][tempos] == min(matriz[voltas]):  
                lista_pelos_tempos.append(tempos)  

    for i in range(6):
        lista_pelas_voltas.append(matriz[i][lista_pelos_tempos[i]])

    volta = lista_voltas.index(min(lista_pelas_voltas))
    tempo = min(lista_voltas)
    piloto = matriz[volta].index(tempo) + 1
    
    tupla = (volta + 1, tempo, piloto)

    
    
    return tupla