def qtd_divisores(numero):
    """Esta função calcula o número de divisores de um número qualquer
    int -> int"""
    qtd = []
    for x in range(1,numero+1):
        if numero%x == 0:
            qtd.append(x)
    return len(qtd)