def repetidos(lista):
    '''função que recebe uma lista de numeros inteiros,e
    retorna o numero de vezes que um elemento da lista  igual 
    ao elemento anterior. list -> int'''
    cont = 0
    i = 0
    while i < len(lista):
        if lista[i] == lista[i - cont]
           cont = cont + 1
        i = i +1
    return cont