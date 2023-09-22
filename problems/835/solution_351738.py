def melhor_volta(matriz):
	'''função que recebe matriz de voltas 
    com tempos e verifica quem fez a melhor volta, com que
    tempo e em que volta, e retorna tupla com dados nessa ordem
    list--> tuple'''

    lista_tempos = []  #abre lista vazia para tempos
    lista_voltas = [] #abre lista vazia para voltas
    

    for voltas in range(6):  #percorre todas as voltas
        for tempos in range(10):  #percorre todos os tempos de cada volta
            if matriz[voltas][tempos] == min(matriz[voltas]):  #se for o menor tempo da volta:    
                lista_tempos.append(tempos)  #captura os índices dos menores tempos de cada volta

    for i in range(6): #percorre elementos do intervalo para criar lista das voltas
        lista_voltas.append(matriz[i][lista_tempos[i]])

    volta = lista_voltas.index(min(lista_voltas))
    tempo = min(lista_voltas)
    piloto = matriz[volta].index(tempo) + 1
    
    tupla = (volta + 1, tempo, piloto)

    #quem fez a melhor volta, qual melhor tempo, que volta foi
    
    return tupla