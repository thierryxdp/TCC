def filtra_pares(tupla):
    def epar(x):
        return x % 2 ==0
    return tuple(filter(epar,tupla))