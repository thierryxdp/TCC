def epar(x):
    """retorna true se um numero for par e false se o numero for impar
    int/float->bool"""
    return x%2==0 
def filtra_pares(t):
    """recebe uma tubla com quatro elementos inteiros como parametro e retorna uma tupla contendo apenas os elementos pares da tupla original, em ordem
    tuple->tuple"""
    pares=[]
    
    if epar(t[0]):
        pares=pares+(t[0],)
    elif epar(t[1]):
        pares=pares+(t[1],)
    elif epar(t[2]):
        pares=pares+(t[2],)
    elif epar(t[3]):
        pares=pares+(t[3],)
    return pares