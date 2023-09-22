def melhor_volta(matriz):
    """Dada uma matriz com os tempos das 6 voltas de 10 corredores que participaram de uma corrida de kart, a função retorna uma tupla dizendo quem fez a melhor volta da prova, em que tempo e em que volta; list -> tuple"""
    
    lista = [0,0,0]
    lista_tempos = []
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            list.append(lista_tempos,matriz[i][j])
    
    minimo = min(lista_tempos)
    
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[i][j] == minimo:
                lista[0] = i+1
                lista[1] = matriz[i][j]
                lista[2] = j+1
    return tuple(lista)