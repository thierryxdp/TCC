def qtd_divisores(numero):
    """Função que dado um número, calcula o número de divisores. int -> int"""
    qtd = []
    for d in range(1,numero+1):
        if numero%d == 0:
            qtd.append(d)
    return len(qtd)