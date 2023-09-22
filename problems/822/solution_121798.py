def repetidos (lista):
    '''função que recebe uma lista de números e retorna o número de vezes que um elemento se repete ao seu precessor.
    list -> int'''
    
    indice = 0
    ocorrencias = 0
    
    while indice< len(lista):
        if lista[indice] == lista[indice-1]:
            ocorrencias = ocorrencias + 1
        indice = indice + 1
    return ocorrencias