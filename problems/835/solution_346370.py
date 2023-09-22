def melhor_volta (matriz):
    '''Funcao que, dada uma matriz, retorna quem fez a melhor volta, em quanto tempo e em que volta.
    list->tupla'''
    
    corredores = (1,2,3,4,5,6)
    voltas = (1,2,3,4,5,6,7,8,9,10)
    tupla = ()
    for i in corredores:
        for j in voltas:
            if matriz[i][j] < corredores[1]:
                tupla = (i+1,matriz[i][j],j+1)
    return tupla