#Start your python function here
def filtro(filtra_pares[a,b,c,d]):

    a = filtra_pares[0]
    b = filtra_pares[1]
    c = filtra_pares[2]
    d = filtra_pares[3]
    par = ()
    if a%2 == 0:
        par = par + (a,) 
    if b%2 == 0:
        par = par + (b,) 
    if c%2 == 0:
        par = par + (c,)
    if d%2 == 0:
        par = par + (d,)
    
    return par