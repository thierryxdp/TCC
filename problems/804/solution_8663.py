def filtra_pares(tupla):
    """retorna uma tupla somente com os seus itens pares
    tupple -> tupple"""
    if tupla[0] % 2 != 0:
        return tupla[1:4]
    if tupla[1] % 2 != 0:
        return tupla[0] + tupla[2:4]
    if tupla[0] % 2 and tupla[1] % 2 != 0:
        return tupla[2:4]
    if tupla[3] % 2 != 0:
        return tupla[0:3] + tupla[3:4]