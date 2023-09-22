def melhor_volta(matriz):
    """A seguinte função irá receber a matriz de voltas com os
    tempos e assim verificar quem fez o melhor tempo pelas voltas
    fazendo assim com que o tempo em em que voltta, retornando a tupla
    com os dados nesta ordem. list-->tuple"""
    lista_pelos_tempos = []  #abre lista vazia para tempos
    lista_pelas_voltas = [] #abre lista vazia para voltas
    

    for voltas in range(6):  #percorre todas as voltas
        for tempos in range(10):  #percorre todos os tempos de cada volta
            if matriz[voltas][tempos] == min(matriz[voltas]):  #se for o menor tempo da volta:    
                lista_pelos_tempos.append(tempos)  

    for i in range(6): 
        lista_pelas_voltas.append(matriz[i][lista_tempos[i]])

    volta = lista_pelas_voltas.index(min(lista_pelas_voltas))
    tempo = min(lista_voltas)
    piloto = matriz[volta].index(tempo) + 1
    
    tupla = (volta + 1, tempo, piloto)

   
    
    return tupla