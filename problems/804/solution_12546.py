def filtra_pares (t):
    """ filtragem de números pares em ordem
    tuple (4 elementos) -> tuple"""
    resposta = ()
    if t[0] % 2 == 0:
        resposta  += (t[0],)
        if t[1] % 2 == 0:
            resposta += (t[1],)
            if t[2] % 2 == 0:
                resposta += (t[2],)
                if t[3] % 2 == 0:
                    resposta += (t[3],)
                    return resposta