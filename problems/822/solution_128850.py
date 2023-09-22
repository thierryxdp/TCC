def repetidos(lista):
    ''' funçao que recebe como entrada uma lista de numeros e retorna o numero de vezes
    que um elemento da lista e igual ao elemento anterior
    list-->int'''
    i=0
    numvezes=0
    while i+1<len(lista):
        if lista[i] ==lista[i=1]:
            numvezes = nimvezes=1
         i=i+1
     return numvezes