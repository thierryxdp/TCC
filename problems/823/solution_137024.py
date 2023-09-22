def faltante(lista):
    """retorna o numero faltante correspondente a peça da lista; list -> int"""
    a=list(range(1,len(lista)))
    for x in lista:
        if x != a[x-1]:
            return x