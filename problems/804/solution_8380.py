def filtra_pares(a):
    """kfnkfnksnfk
    Entrada: Tuple(Int, Int, Int, Int)
    Saída: Tuple(Int, Int, Int, Int)"""
    tuplapar = () 
    a_par = (int(a)%2)
    b_par = (int(b)%2)
    c_par = (int(c)%2)
    d_par = (int(d)%2)
    
    if a_par == 0:
        tuplapar = tuplapar + (a,)  
    if b_par == 0:
        tuplapar = tuplapar + (b,) 
    if c_par == 0:
        tuplapar = tuplapar + (c,) 
    if d_par == 0:
        tuplapar = tuplapar + (d,)
    return tuplapar