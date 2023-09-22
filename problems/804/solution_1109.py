def par(n):
    """Função que retorna um número se ele for par, mas não retorna nada se for ímpar."""
    if n%2==0:
        return n
    else:
        return()

def filtra_pares(x):
    """Função que recebe como entrada uma tupla com quatro elementos inteiros, e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que estavam."""
    x= [a,b,c,d]
    return list(filter(par,x))