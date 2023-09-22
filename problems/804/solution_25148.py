'''recebe uma tupla t e retorna uma nova tupla contendo os elementos pares da tupla t
Assinatura: tuple -> tuple'''
def eh_par(x):
    if x%2==0:
        return x
    else:
        return
def filtra(w):
    return eh_par(w[0]),eh_par(w[1]),eh_par(w[2]),eh_par(w[3])
def filtra_pares(x):
    return tuple(filtra(x))