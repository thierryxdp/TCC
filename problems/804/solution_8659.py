def filtra_pares(tupla):
    """retorna uma tupla somente com os seus itens pares
    tupple -> tupple"""
    if tupla[0] % 2 != 0:
        return tupla[1:3]