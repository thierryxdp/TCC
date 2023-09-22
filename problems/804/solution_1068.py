def filtra_pares(a):
    """avalia uma tupla com 4 números inteiros e retorna os números pares dessa tupla"""
    resto = int(a[:4])%2
    if resto == 0:
        return a
    else:
        return none