def melhor_volta(matriz):
    '''função que recebe uma matriz com as informações do resultado de uma corrida de 10 voltas feitas por 6 corredores e retorna a melhor volta, o tempo e em qual volta foi.
    list-->tuple'''
    minimo=min(matriz[0])
    crrdr=1
    for i in matriz:
        if min(i)<=minimo:
            minimo=min(i)
            crrdr=matriz.index(i)+1
    return crrdr,minimo,matriz[crrdr-1].index(minimo)+1