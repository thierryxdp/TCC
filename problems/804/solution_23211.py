#Start your python function here
def filtra_pares(x):
    """..."""
    def par(n):
        if n%2 == 0:
            return n
    
    a = par(x[0])
    b = par(x[1])
    c = par(x[2]) 
    d = par(x[3])
    
    if a == None:
        if b == None:
            if c == None:
                if d == None:
                    return ()
        elif c == None:
            if d == None:
                return (b)
        elif d == None:
            return (b,c)
        else: (b,c,d)
	elif b == None:
        if c == None:
            if d == None: