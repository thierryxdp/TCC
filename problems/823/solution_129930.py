def faltante(L:list)->int:
    """Dada uma lista, estabelece uma sequencia do menor ao maior, e retorna qual peça falta."""
    proximo=1
    ordenada=list.sort(L)
    while proximo in ordenada:
        proximo=proximo+1
        return proximo