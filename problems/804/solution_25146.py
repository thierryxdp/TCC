'''recebe uma lista l e retorna uma nova tupla contendo os elementos pares da tupla t
Assinatura: tuple -> tuple'''
def eh_par(x):
    if x%2==0:
        return x
    else:
        return
def filtra_pares(l):
    return tuple(eh_par(l[0]),eh_par(l[1]),eh_par(l[2]),eh_par(l[3]))