"""Retorna uma tupla só com os pares da original"""
def filtra_pares (a,b,c,d):
    if a//2 or b//2 or c//2 or d//2:
        return filtra_pares(a,b,c,d)