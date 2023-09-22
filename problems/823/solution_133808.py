def faltante(lista):
    '''Daada uma função com números inteiros numerados de 1 a N,
    descobre o numero que esta nesse intervalo. list->int '''
    
    indice=0
    num_anterior = lista[-1] -1
    proximo_num = 1
    while num_anterior != -1:
        if proximo_num in lista:
            proximo_num+=1
            
        else:
            return proximo_num