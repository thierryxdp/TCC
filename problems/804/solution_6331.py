'''Função que recebe:
uma tupla (t) contendo 4 elementos int;
e retorna apenas os pares da tupla pelo sistema de filtragem;
tupla-> tupla'''
def filtra_pares(t):
    n = ()
    if t[0] %2==0:
        tuplapar = n + (t[0],)
        return tuplapar
    if t[2] %2==0:
        tuplapar = n + (t[2],)