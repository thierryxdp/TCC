def soma_h(numero):
    """função que retorna a soma de H
    int -> float"""
    h=0
    for n in range(1,numero+1):
        h += 1/n
    return round(h,2)