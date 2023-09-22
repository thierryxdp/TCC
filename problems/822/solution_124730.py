def repetidos(lista):
    '''	retorna a quantidade de numeros repetidos na lista
    lista -> int'''
    i = 1
    soma = 0
    while i < len(lista):
        if lista[i] == (lista[i-1]):        
            soma = soma + 1
        i = i + 1
    return soma