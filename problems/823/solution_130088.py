def faltante(lista):
    """funcao que dado uma lista de numeros inteiros de 1 a N retorna o numero inteiro deste intervalo faltante 
    lista -> int"""
    list.sort(lista)
    j = 0
    n = 1
    while j < len(lista):
        if lista[j] == j+1:
            n = lista[j] + 1
        j += 1
    return n