def soma_h(numero):
    """Essa função recebe um numero e retorna a soma da divisão de 1 por h, h vezes
    int -> int"""
    h = 0
    for x in range(1,numero+1):
        h += 1/x
    return round(h,2)