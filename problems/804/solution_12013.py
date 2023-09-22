def par(n):
    """verifica se um numero inteiro n é par"""
    return(n%2)==0

def filtra_pares(tp):
    if par(tp[0]):
        return (tp[0],)
    if par(tp[1]):
        return (tp[0], tp[1],)
    if par(tp[2]):
        return (tp[0], tp[1], tp[2],)
    if par(tp[3]):
        return (tp[0], tp[1], tp[2], tp[3])