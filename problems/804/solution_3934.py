def filtra_pares(t,u,p,l,):
    """Dado uma tupla com quatro elementos inteiros, retorna uma tuplas com apenas pares da tupla original."""
    tupla=()
    if int(t%2==0):
        tupla=tupla+(t,)
    if int(u%2==0): 
        tupla=tupla+(u,)
    if int(p%2==0):
        tupla= tupla+(p,)
    if int(l%2==0): 
        tupla=tupla+(l,)
    return tupla