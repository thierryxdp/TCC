def repetidos(lista):
    ''' função que recebe uma lista e retorna a quantidade de 
    vezes que um elemento da lista e igual ao elemento anterior.
    list -> int'''
    i=0
    contador=0
    while i <  len(lista):
        if lista[i] == lista[i-1]:
            contador= contador+1
        i=i+1
    return contador