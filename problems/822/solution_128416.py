def repetidos(lista_num):
    """retorna a quantidade de numeros repetidos existem em uma lista qualquer
    list -> int"""
    cont, i, rep = 1, 0, 0
    while i < len(lista_num):
        if lista_num[i] == lista_num[i-1]:
            rep += 1
        i += 1
    return rep