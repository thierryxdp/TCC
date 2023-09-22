def qtd_divisores(numero):
    soma=0
    i=1
    for i in range(numero):
        if numero%i==0:
            soma=soma+i
    return soma