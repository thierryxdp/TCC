#Start your python function here
def filtra_pares(t:tuple)->tuple:
    
    """Funcao que recebe uma tupla com quatro elementos inteiros como parametro e
    que retorna uma nova tupla contendo apenas os elementos pares da tupla original.
     """
    
    par = ()
    if t[0]%2 == 0: 
        par = par + (t[0],)
    if t[1]%2 == 0:
        par = par + (t[1],)
    if t[2]%2 == 0:
        par = par + (t[2],)
    if t[3]%2 == 0:
        par = par + (t[3],)
    return par