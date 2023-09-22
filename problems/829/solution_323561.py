def soma_h(n):
    ''' Função que calcula o valor de H. '''
    resultado = 0
    for i in range (1, n + 1):
        soma = (1/i)
        resultado += soma
    return round(resultado, 2)