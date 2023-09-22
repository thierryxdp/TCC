def repetidos(lista):
    ''' A função recebe uma lista de números e retorna o número de vezes que um elemento é igual ao anterior
    list-> int'''
    i = 1
    repetição = 0
    while i< len(lista):
        if lista[i] == lista[i-1]:
            repetição = repetição + 1
        i = i + 1
    return repetição