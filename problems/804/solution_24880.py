def e_par(x):
    """funcao booleana que verifica se um 
    numero inteiro x e par
    int -> bool"""
    return x%2 == 0

def filtra_pares(t):
    """funcao que contem uma tupla de 4 numeros inteiros
    e retorna uma tupla apenas com os elementos pares da 
    tupla original
    tup -> tup"""
    pares = ()
    if e_par(t[0]):
        pares = pares + (t[0],)
    if e_par(t[1]):
        pares = pares + (t[1],)
    if e_par(t[2]):
        pares = pares + (t[2],)
    if e_par(t[3]):
        pares = pares + (t[3],)
    else:
        return ()
        return pares