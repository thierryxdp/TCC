def par(n):
    """verifica se um numero inteiro n é par"""
    return(n%2)==0

def filtra_pares(tp):
    x=()
    if par(tp[0]):
        x= x + (tp[0],)
    if par(tp[1]):
        x= x + (tp[1],)
    if par(tp[2]):
        x= x + (tp[2],)
    if par(tp[3]):
        x= x + (tp[3],)
        return x