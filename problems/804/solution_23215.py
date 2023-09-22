#Start your python function here
def filtra_pares(x):
    """..."""
    def par(n):
        if n%2 == 0:
            return n
        else:
            return 0
    
    a = par(x[0])
    b = par(x[1])
    c = par(x[2]) 
    d = par(x[3])
    
    return (a,b,c,d)