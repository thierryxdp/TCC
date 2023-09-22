def filtra_pares(t,u,p,l,):
    """Dado uma tupla com quatro elementos inteiros, retorna uma tuplas com apenas pares da tupla original."""
    tupla= ()
    if (t%2==0):
        tupla=tupla+(t,)
    if (u%2==0): 
        tupla=tupla+(u,)
    if (p%2==0):
        tupla= tupla+(p,)
    if (l%2==0): 
        tupla=tupla+(l,)
    return tupla