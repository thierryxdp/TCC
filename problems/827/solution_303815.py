def qtd_divisores(numero):
    div=1
    for i in range(1,int(numero/2+1)):
        if numero % i == 0:
            div+=1
    return div