def PAR(x):
    return (x%2) == 0
def filtra_pares(t):
    """Função que recebe uma tupla com quatro elementos inteiros
    e retorna uma nova tupla com apenas os elementos pares da
    tupla original.
    tup(int)->tup(int)
    """
    NePar = ()
    if PAR(t[0]):
        NePar = NePar + (t[0],)
    elif PAR(t[1]):
         NePar = NePar + (t[1],)
    elif PAR(t[2]):
        NePar = NePar + (t[2],)
    elif PAR(t[3]):
        NePar = NePar + (t[3],)
        return NePar