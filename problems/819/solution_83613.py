def filtraMultiplos(lista,n):
    '''retorna outra lista contendo os n° divisíveis; tem 
    como entrada a lista e um n°;list, int->list '''
    lf= []
    cont= 0
    while cont<= len(lista):
        if lista[cont]%n ==0:
            lf = lf + (lista[cont],)
        cont = cont + 1
    return lf