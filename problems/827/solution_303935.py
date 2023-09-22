def qtd_divisores(numero):
    contador=0
    for elemento in range(1,numero+1):
        if numero%elemento==0:
            contador=contador+1
    return contador