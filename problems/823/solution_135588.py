def faltante(lista):
    """retorna o numero fora da lista correspondente a uma peça faltante; list -> int"""
    a=1
    if 1 not in lista:
        return 1
    while (lista[a]-lista[a-1]==1):
        a+=1
        if a==len(lista):
            return lista[len(lista)]+1
    return lista[a]