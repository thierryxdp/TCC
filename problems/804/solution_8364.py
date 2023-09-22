def filtra_pares(a,b,c,d):
    """kfnkfnksnfk
    Entrada: Tuple(Int, Int, Int, Int)
    Saída: Tuple(Int, Int, Int, Int)"""
    filtragem = (2,4,6,8)
    tuplapar = () 
    a_par = a//filtragem   
    b_par = b//filtragem
    c_par = c//filtragem
    d_par = d//filtragem
    
    if a_par:
        tuplapar = tuplapar + a  
    if b_par:
        tuplapar = tuplapar + b 
    if c_par:
        tuplapar = tuplapar + c 
    if d_par:
        tuplapar = tuplapar + d 
    return tuplapar