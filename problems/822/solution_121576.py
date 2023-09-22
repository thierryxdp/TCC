def repetidos(lista):
    '''funcao que dado uma lista de numeros
    retorn quantas vezes um elemento é igual
    ao elemento anterior; list -> int'''
    
    i = 1
    repetidos = 0
    while i < len(lista):
        if lista[i] == lista[i-1]:
            repetidos = repetidos + 1
        i = i + 1
    return repetidos