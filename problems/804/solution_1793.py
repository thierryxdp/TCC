#Start your python function here
def filtra_pares(t1):
    """Funcao que retorna uma tupla feita somente de numeros pares, com base
    em uma tupla escolhida."""
    
 	(a, b, c, d) = t1
    t2=()
    
    if a%2 == 0:
        t2 = t2+(a,)
    if b%2 == 0:
        t2 = t2+(b,)
    if c%2 == 0:
        t2 = t2+(c,)
    if d%2 == 0:
        t2 = t2+(d,)
    return t2