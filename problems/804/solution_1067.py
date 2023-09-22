def filtra_pares(a):
    """avalia uma tupla com 4 números inteiros e retorna os números pares dessa tupla"""
    resto1 = a[1]%2
    resto2 = a[2]%2
    resto3 = a[3]%2
    resto4 = a[4]%2
    if resto1==0 and resto2==0 and resto3==0 and resto4==0:
        return a[:4]