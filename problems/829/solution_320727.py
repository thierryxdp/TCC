def soma_h(numero):
    if numero <= 0:
        return "invalido"
    else:
        U = 1
        r = 0
        while U <= numero:
            r = r+1/U
            U = U + 1
        return r