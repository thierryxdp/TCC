def qtd_divisores(numero):
    soma = 0
    for i in list(range(1,numero+1)):
        if numero%i==0:
            soma = soma + 1
    return soma