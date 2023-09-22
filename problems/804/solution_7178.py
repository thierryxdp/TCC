def filtra_pares(t):
    """Funcao que recebe uma tupla com quatro elementos inteiros como parametro, e retorne uma nova tupla contendo apenas os elementos pares da tupla original, na mesma ordem em que se encontravam,
    tupla -> tupla"""
    tn = tuple()
    if t[0]%2 == 0:
        tn = tn + (t[0],)
    if t[1]%2 == 0:
        tn = tn + (t[1],)
    if t[2]%2 == 0:
        tn = tn + (t[2],)
    if t[3]%2 == 0:
        tn = tn + (t[3],)
        return tn