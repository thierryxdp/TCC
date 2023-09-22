def repetidos(lista):
    """Função que recebe como entrada uma lista de numeros e retorna o numero de vezes que um elemento da lista é igual ao elemento anterior
       list -> int"""
    indice = 1
    proximo = 0
    while indice < len(lista):
        if lista[indice] == lista[indice-1]:
            proximo += 1
        indice += 1
    return proximo