def par(n):
    """Função que retorna um número se ele for par, mas não retorna nada se for ímpar."""
    if n%2==0:
        return True
    else:
        return False

def filtra_pares(a,b,c,d):
    """Função que recebe como entrada uma tupla com quatro elementos inteiros, e retorna uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que estavam."""
    return list(filter(par,[a,b,c,d]))