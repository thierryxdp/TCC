def repetidos(lista):
    """Essa função recebe uma lista de números inteiros e 
    retorna o número de vezes que o elemento da lista é igual
    ao elemento anterior. list->int"""
    contador = 0
    primeiro = 0
    i = lista[:]
    while primeiro < len(lista):
        i = lista[primeiro]
        if i == i+1:
            contador = contador + 1
        primeiro = primeiro +1 
    return contador