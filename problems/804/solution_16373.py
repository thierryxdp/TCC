def par(x):
    """Verifica se um número é ou não par"""
    if x%2==0:
        return True
    else:
        return False
def filtra_pares(a,b,c,d):
    return list(filter(par,a),filter(par,b),filter(par,c),filter(par,d),