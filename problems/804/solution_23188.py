#Start your python function here
def filtra_pares(x):
    """..."""
    def par(n):
        if n%2 == 0:
            return n
    
    a = par(x[0]) == 0
    b = par(x[1]) == 0
    c = par(x[2]) == 0
    d = par(x[3]) == 0
    
    return a,b,c,d