"""Retorna uma tupla só com os pares da original
tuple->tuple"""
def filtra_pares (a,b,c,d):
    if a//2 or b//2 or c//2 or d//2:
        return tuple(filtra_pares(a,b,c,d))