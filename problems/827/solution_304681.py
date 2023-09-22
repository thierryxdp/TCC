def qtd_divisores(numero):
    'função que dado um numero conta quantos divisores ele tem'
    resultado = 0
    for i in range(1, numero+1):
        if numero%i == 0:
            resultado =+ 1
    return resultado