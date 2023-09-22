def qtd_divisores(natural):
    soma = 0
    for corredor in range(natural):
        if corredor == 0:
            soma = soma
        elif natural%corredor == 0:
            soma = soma + 1
    return soma