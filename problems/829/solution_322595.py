def soma_h(numero):
    """ função que retorna o valor de H com N termos
    int -> float"""
    H = 1
    i = 2
    while i <= numero:
        H = H + 1 / i
        i = i + 1
    return round(H,2)