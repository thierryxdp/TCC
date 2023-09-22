def repetidos (lista):
    '''Retorna o número de vezes que um elemento da lista 
    é igual ao anterior
    lista-> int'''
    indice = 0
    repeticao = 0
    while indice < len( lista):
        if lista[indice] == lista [indice -1]:
            repeticao += 1
        indice += 1
    return repeticao