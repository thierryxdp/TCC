def soma_h(numero):
    """Função que dado um número, retorna a soma da divisão de 1 por h em h vezes. int -> int"""
    h = 0
    for n in range(1,numero+1):
        h += 1/n
    return round(h,2)