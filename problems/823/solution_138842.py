def faltante(lista_pecas):
    """retorna o numero da peca faltante
    lista -> int"""
    lista_pecas.sort()
    i = 0
    while i < len(lista_pecas):
        if lista_pecas[i+1] != lista_pecas[1]+1:
            return lista_pecas[i]+1