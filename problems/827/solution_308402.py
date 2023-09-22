def qtd_divisores(numero):
    total = 0
    divisores = 1
    while numero%divisores!=0:
        divisores = divisores + 1
    else:
        total = total + 1
    return total