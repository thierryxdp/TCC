def melhor_volta (matriz):
    '''Funcao que, dada uma matriz, retorna quem fez a melhor volta, em quanto tempo e em que volta.
    list->tupla'''
    
    corredores = randint (1,6)
    voltas = randint (1,10)
    
    for i in corredores:
        for j in voltas:
            if matriz[i][j] < corredores[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return