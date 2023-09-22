def faltante(lista):
    """funcao que dado uma lista de numeros inteiros de 1 a N retorna o numero inteiro deste intervalo faltante 
    list -> int"""
    list.sort(lista)
    j = 0
    s = 1
    while j < len(lista):
        if lista [j] == j+1:
            s = lista [j] + 1
    return j