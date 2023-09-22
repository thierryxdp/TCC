def qtd_divisores(natural):
    soma = 0
    corredor = 1
    for corredor in range(natural):
        if corredor == 0:
            soma = soma
        if natural%corredor == 0:
            soma = soma + 1
    return soma