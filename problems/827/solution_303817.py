def qtd_divisores(numero):
    div=0
    for i in range(1,numero):
        if numero % i == 0:
            div+=2
    return div