'''Função que recebe:
uma tupla (t) contendo 4 elementos int;
e retorna apenas os pares da tupla pelo sistema de filtragem;
tupla-> tupla'''
def filtra_pares(t):
    n = ()
    if t[0] %2==0:
        return n
    elif t[1] %2==0:
        n = n + (t[1],)
        return n
    elif t[2] %2==0:
        n = n + (t[2],)
        return n
    elif [3] %2==0:
        n = n + (t[3],)
        return n
    else:
        t[4] %2==0:
        n = n + (t[4],)
        return n