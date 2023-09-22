def soma_h(numero):
    '''Dado um número inteiro e positivo, retorna a soma
    1 + 1/2 + 1/3 + 1/4 + 1/numero.
    int -> float'''
    resultado = 0
    for i in range(1,numero+1):
        resultado = resultado + (1/i)
    return round(resultado,2)