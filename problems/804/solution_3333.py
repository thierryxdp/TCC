def filtra_pares(tupla):
    """Recebe uma tupla com quatro elementos inteiros
    e retorna apenas os elementos pares em uma nova tupla."""
    t= ()
    if tupla[0]%2 == 0:
        t = t + (tupla[0],)
    if tupla [1]%2 ==0:
        t = t + (tupla[1],)
    if tupla [2]%2 ==0:
        t = t + (tupla[2],)
    if tupla [3]%2 ==0:
        t = t + (tupla[3],)
    return t