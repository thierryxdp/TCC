def soma_h(numero):
    """Funcao recebe um numero e retorna a soma entre as razoes 1/1 até 1/N
    int -> int"""
    h = 0
    for i in range(1,numero+1):
        h = h + 1/i
        h1 = round(h, 2)
    return h1