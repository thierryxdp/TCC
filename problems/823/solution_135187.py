def faltante(lista):
    '''dada uma lista de numeros inteiros de 1 a n, com n-1
    elementos, essa funcao nos devolve qual é o numero que
    esta faltando na lista
    list-->int.'''
    i=0
    lista1=sorted(lista)
    while i<len(lista1):
        if i+1!=lista1[i]:   
            return i+1
        i=i+1
    return len(lista1)+1