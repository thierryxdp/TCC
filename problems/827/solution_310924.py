def qtd_divisores(numero):
    """Esta função recebe um numero e calcula o numero de divisores
    int -> int"""
    qtd = []
    for i in range(1,numero+1):
        if numero%i == 0:
            qtd.append(i)
    return len(qtd)