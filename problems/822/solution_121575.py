def repetidos(lista):
    '''funcao que dado uma lista de numeros
    retorn quantas vezes um elemento é igual
    ao elemento anterior; list -> int'''
    
    i = 0
    repetidos = 0
    while i < len(lista):
        if lista[i+1] == lista[i]:
            repetidos = repetidos + 1
        i = i + 1
    return repetidos