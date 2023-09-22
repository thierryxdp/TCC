#Start your python function here
#filtra os elementos pares de uma tupla
#assinatura: tuple --> tuple

def filtra_pares(t):
    resultado = filter(lambda x:x % 2 == 0, t)
    return tuple(resultado)