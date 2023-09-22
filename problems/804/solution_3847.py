def filtra_pares (tupla) :
    """Funcao que recebe uma tupla com quatro elementos inteiros e retorna uma nova tupla apenas com os elementos pares da tupla original, na mesma ordem"""
    t = ()
    if tupla[0]%2 == 0 :
        t = t + (tupla[0],)
    if tupla[1]%2 == 0 :
        t = t + (tupla[1],)
    if tupla[2]%2 == 0 :
        t = t + (tupla[2],)
    if tupla[3]%2 == 0 :
        t = t + (tupla[3],)
    return t