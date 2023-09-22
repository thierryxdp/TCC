def filtra_pares(tupl):
    
    """Dado uma tupla com quatro elementos inteiros, retorna uma tuplas com apenas pares da tupla original."""
    tupla=()
   
    if (tupl[0]%2==0):
        tupla=tupla+(tupl[0],)
    if (tupl[1]%2==0): 
        tupla=tupla+(tupl[1],)
    if (tupl[2]%2==0):
        tupla= tupla+(tupl[2],)
    if (tupl[3]%2==0): 
        tupla=tupla+(tupl[3],)
    return tupla