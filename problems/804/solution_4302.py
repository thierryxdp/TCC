def par(n):
    """delimita um parâmetro para definir os valores pares de uma função;
    bool -> bool"""
    if n % 2 == 0:
        return True
    else:
        return False
    
def filtra_pares (a):
    """"calcula e retorna os valores pares da tupla;
    int -> int"""
    return tuple(filter(par,a))