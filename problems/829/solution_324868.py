def soma_h(numero):
    """Essa função recebe um numero e retorna a soma da divisão de 1 por h, h vezes int -> int"""
    h = 0
    for i in range(1,numero+1):
        h += 1/i
    return round(h,2)