def repetidos(lista):
    '''Recebe uma lista de números, e retorna o número de vezes que um elemento da lista 
    é igual ao elemento anterior;
    list -> int'''
    
    i = 0
    ocorr = 0

    while i < len(lista)-1:
        if lista[i+1] == lista[i]:
            ocorr += 1
        i += 1

    return ocorr