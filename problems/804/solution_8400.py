def filtra_pares(b):
    """A função receberá quatro valores inteiros, e retornará uma nova tupla
    apenas com os valores inteiros pares da tupla original. Todos os valores
    pares deverão estar na mesma ordem em que estavam.
    Entrada: Tuple(Int, Int, Int, Int)
    Saída: Tuple(Int, Int, Int, Int)"""
    tuplapar = () 
    b_par = b//2
    
    if b_par == 0:
        tuplapar = tuplapar + (b,) 
    return tuplapar