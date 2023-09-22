def filtra_pares(a,b,c,d):
    """Funcao que dado 4 numeros, retorna apenas os pares na mesma ordem de entrada"""
    if a%2==0 or b%2==0 or c%2==0 or d%2==0:
        return a,b,c,d
    else:
        return ()