def qtd_divisores(x):
    soma=0
    for valor in range(1,x+1):
        if x%valor==0:
            soma=soma+1
    return soma