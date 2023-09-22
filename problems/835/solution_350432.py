def melhor_volta(matriz):

    lista_tempos = []  #abre lista vazia para tempos
    lista_voltas = [] #abre lista vazia para voltas
    

    for voltas in range(4):  #percorre todas as voltas
        for tempos in range(6):  #percorre todos os tempos de cada volta
            if matriz[voltas][tempos] == min(matriz[voltas]):  
    
                lista_tempos.append(tempos)  #captura os índices dos menores tempos de cada volta

    for i in range(4): #percorre elementos do intervalo para criar lista das voltas
        lista_voltas.append(matriz[i][lista_tempos[i]])

    volta = lista_voltas.index(min(lista_voltas))
    tempo = min(lista_voltas)
    piloto = matriz[volta].index(tempo) + 1
    
    tupla = (piloto, tempo, volta + 1)

    #quem fez a melhor volta, qual melhor tempo, que volta foi
    
    return tupla