'''recebe uma tupla t e retorna uma nova tupla contendo os elementos pares da tupla t
Assinatura: tuple -> tuple"
def eh_par(x):
    if x%2==0:
        return x
    else:
        return
    
def filtra_pares(t):
    return tuple(eh_par(t[0]),eh_par(t[1]),eh_par(t[2]),eh_par(t[3]))
#Start your python function here