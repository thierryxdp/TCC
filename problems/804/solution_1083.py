def filtra_pares(a):
    """avalia 4 números inteiros de entrada em uma tupla e retorna os números pares da
mesma"""
    resto1 = a[0]%2
    resto2 = a[1]%2
    resto3 = a[2]%2
    resto4 = a[3]%2
    if resto1==0 and resto2==0 and resto3==0 and resto4==0:
        par = a
        return par