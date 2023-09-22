def soma_h(numero):
    '''Realiza a soma 1 + 1/2 + 1/3 +...+ 1/numero.
    int -> float'''
    H = 0
    lista = range(1, numero+1)
    if numero == 0:
        return round(0,2)

    for n in lista:
        H = H+ 1/n

    return round(H,2)