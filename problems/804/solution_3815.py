def filtra_pares(tupla):
    """Funcao que recebe uma tupla com 4 elementos inteiros e retorna somente os pares desta tupla"""
    par = ()
    if tupla[0]%2 == 0:
        par = par + (tupla[0],)
    if tupla[1]%2 == 0:
        par = par + (tupla[1],)
    if tupla[2]%2 == 0:
        par = par + (tupla[2],)
    if tupla[3]%2 == 0:
        par = par + (tupla[3],)
    return par