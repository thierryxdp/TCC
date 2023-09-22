def faltante(L:list)->int:
    """Dada uma lista, estabelece uma sequencia do menor ao maior, e retorna qual peça falta."""
    proximo=1
    while proximo in list.sort(L):
        proximo=proximo+1
    return proximo