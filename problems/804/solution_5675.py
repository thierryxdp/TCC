def filtra_pares(x):
    """Calacula e retorna uma nova tupla com numeros pares de uma tupla original"""
    if (x<0) % 2==0:
        return x
    if (x>0) % 2==0:
        return x
    else:
        return 0