def qtd_divisores(numero):
    soma=0
    for i in range(numero):
        if numero%i==0:
            soma=soma+1
    return soma