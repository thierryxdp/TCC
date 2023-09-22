def fatorial(numero):
    if numero < 0:
        return "invalido"
    elif numero == 0:
        return 1
    else:
        U = 1
        r = 1
        while U <= numero:
            r = U * r
            U = U + 1
        return r