def qtd_divisores(numero):
    div=0
    for i in range(1,numero+1):
        if numero % i == 0:
            div+=1
    return div