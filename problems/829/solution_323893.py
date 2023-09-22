def soma_h(n):
    '''Função que dado o valor de N, calcula
    o somatório de H com N '''
    'int---->float'
    soma = [1]
    for numero in range(n, n+1):
        soma.append((numero)**-1)
        somatorio = sum(soma)
        resultado=round(somatorio, 2)
    return resultado