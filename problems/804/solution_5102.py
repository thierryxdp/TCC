def filtra_pares(t,u,p,l,):
    """Dado uma tupla com quatro elementos inteiros, retorna uma tuplas com apenas pares da tupla original."""
    tupla=()
    if (t[0]%2==0):
        tupla=tupla+(t[0],)
    if (u[1]%2==0): 
        tupla=tupla+(u[1],)
    if (p[2]%2==0):
        tupla= tupla+(p[2],)
    if (l[3]%2==0): 
        tupla=tupla+(l[3],)
    return tupla