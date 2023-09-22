def melhor_volta (matriz):
    '''Funcao que, dada uma matriz, retorna quem fez a melhor volta, em quanto tempo e em que volta.
    list->tupla'''
    
    tupla = []
    for i in range(6):
        for j in range(10):
            if matriz[i][j] < tupla[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla