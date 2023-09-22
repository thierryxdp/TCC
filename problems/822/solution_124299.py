def repetidos(lista):
    """Recebe como entrada uma lista de números e retorna o número de vezes
    que um elemento da lista é igual ao elemento anterior;list->int"""
    contador=1
    vezes=0
    while contador<len(lista):
        if lista[contador]==lista[contador-1]:
            vezes=vezes+1
        contador=contador+1
    return vezes