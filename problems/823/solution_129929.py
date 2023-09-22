def faltante(lista_pecas:list)->int:
    """Dada uma lista, estabelece uma sequencia do menor ao maior, e retorna qual peça falta."""
    proximo=1
    ordenada=list.sort(lista_pecas)
    while proximo in ordenada:
        proximo=proximo+1
        return proximo