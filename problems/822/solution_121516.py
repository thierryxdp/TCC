def repetidos(lista):
    '''dada uma lista, retorna quantas vezes um elemento é igual ao seu antecessor
    list -> int'''
    contador = 0
    i = 0
    if len(lista) == 2:
        if lista[0] == lista[1]:
            return 1
    while i < len(lista):
        if lista[i] == lista[i-1]:
            contador += 1
        i += 1
    return contador