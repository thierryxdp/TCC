def qtd_divisores(x):
    soma=0
    for valor in range(x):
        if x % valor==0:
            soma=soma+1
    return soma