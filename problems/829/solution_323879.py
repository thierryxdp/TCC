def soma_h(n):
    '''Função que dado o valor de N, calcula o somatório de :
    (-1)^n/2n+1'''

    resultado = 1
    numerador = 1
    denominador = 1
    for i in range(n):
        denominador += 1
        numerador = numerador * -1
        soma=numerador/denominador
        resultado=resultado+soma
    return resultado