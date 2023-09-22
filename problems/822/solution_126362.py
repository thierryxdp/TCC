def repetidos(lista):
    '''Função que recebe uma lista de números e verifica quantas
    vezes um elemento da lista é igual ao anterior; lista -> int'''
    i = 1
    contador = 0
    while i < len(lista):
        if lista[i] == lista[i - 1]:
            contador += 1
        i += 1
    return contador