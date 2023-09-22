def repetidos(listaNum):
    '''Funcao que recebe uma lista de numeros e retorna o numero
de vezes que um elemento da lista e igual ao elemento anterior'''
    acumuladora = 0
    i = 0
    list.sort(listaNum)
    while i < len(lista)-1:
        if listaNum[i-1] == listaNum[i]:
            acumuladora = acumuladora + 1
        i = 0
    return ListaNum