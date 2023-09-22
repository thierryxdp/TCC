def melhor_volta(matriz):
    '''função que recebe uma matriz com as 10 voltas de 6 corredores numerados de 1 a 6 e retorna quem fez a melhor 
    volta, em qual tempo e em que volta.
    list -> tuple'''
    
    melhores_tempos = []
    
    for i in range(len(matriz)):
        lista_voltas = []
        for n in range(len(matriz[0])):
            list.append(lista_voltas, matriz[0][n])
        list.sort(lista_voltas)
        list.append(melhores_tempos, lista_voltas[0])
    return melhores_tempos