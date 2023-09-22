def filtra_pares (tupla):
    """ filtragem de números pares em ordem
    tuple (4 elementos) -> tuple"""
    resposta = ()
    if tupla [0] % 2 == 0:
        resposta  =  resposta + (tupla[0],)
        if tupla [1] % 2 == 0:
            resposta = resposta + (tupla[1])
            if tupla [2] % 2 == 0:
                resposta = resposta + (tupla[2])
                if tupla [3] % 2 == 0:
                    resposta = resposta + (tupla[3])
                    return resposta