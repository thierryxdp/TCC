def repetidos(lista):
    '''Função que recebe como entrada uma lista de numeros
     e retorne o numero de vezes que um elemento da lista
     é igual ao elemento anterior;
     list -> int'''
    i = 0
    s = 0
    while (i)<len(lista):
        if lista[i-1] == lista[i]:
            s += 1
        i = i +1
    return s