def repetidos(lista):
    '''Dada uma lista retorna quantas vezes um elemento é igual 
    a um anterior
    list -> list'''
    a = 0
    l = len(lista)
    x = 0
    while True:
        if a == l:
            return x
        if lista[a] == lista[a+1]:
            x += 1
        a += 1