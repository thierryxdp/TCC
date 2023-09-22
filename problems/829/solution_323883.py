def soma_h(n):
    '''Função que dado o valor de N, calcula
    o somatório de H com N '''
    'int---->float'
    
    resultado = 1
    numerador = 1
    denominador = 1
    for i in range(n):
        denominador += 1
        numerador = numerador * -1
        soma=numerador/denominador
        resultado=resultado+soma
    
    for numero in range(2, n+1):
        soma.append((numero)**-1)
        somatorio = sum(soma)
    return round(somatorio, 2)