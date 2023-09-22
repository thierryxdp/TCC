def filtra_parez(a,b,c,d):
    """A função receberá quatro valores inteiros, e retornará uma nova tupla
    apenas com os valores inteiros pares da tupla original. Todos os valores
    pares deverão estar na mesma ordem em que estavam.
    Entrada: Tuple(Int, Int, Int, Int)
    Saída: Tuple(Int, Int, Int, Int)"""
    tuplapar = () 
    a_par = a%2
    b_par = b%2
    c_par = c%2
    d_par = d%2
    
    if a_par == 0:
        tuplapar = tuplapar + (a,)  
    if b_par == 0:
        tuplapar = tuplapar + (b,) 
    if c_par == 0:
        tuplapar = tuplapar + (c,) 
    if d_par == 0:
        tuplapar = tuplapar + (d,)
    return tuplapar