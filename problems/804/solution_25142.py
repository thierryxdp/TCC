'''recebe uma tupla t e retorna uma nova tupla contendo os elementos pares da tupla t
Assinatura: tuple -> tuple'''
def eh_par(x):
    if x%2==0:
        return x
    else:
        return
    
def filtra_pares(w,x,y,z):
    return tuple(eh_par(w),eh_par(x),eh_par(y),eh_par(z))
#Start your python function here