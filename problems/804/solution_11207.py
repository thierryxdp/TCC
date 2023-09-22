def filtra_pares(tupla):
    """recebe uma tupla com 4 valores e retorna os numeros pares dela. str->int."""
    A,B,C,D = tupla
    a = int(A)
    b = int(B)
    c = int(C)
    d = int(D)
    tupla_par = ()
    if (a%2==0):
        tupla_par = tupla_par + (a,)
    if (b%2==0):
        tupla_par = tupla_par + (b,)
    if (c%2==0):
        tupla_par = tupla_par + (c,)
    if (d%2==0):
        tupla_par = tupla_par + (d)
            
    return tupla_par