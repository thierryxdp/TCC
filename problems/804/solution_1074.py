def filtra_pares(x):
    """avalia os 4 números inteiros inseridos e retorna os números pares"""
    resto1 = int(x[0])%2
    if resto1==0:
        return "("+x[0]+")"