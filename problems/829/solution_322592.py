def soma_h(numero):
    """ função que retorna o valor de H com N termos
    int -> float"""
    H = 1
    for x in numero:
        H = (H+1)/x
    return round(H,2)