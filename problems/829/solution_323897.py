def soma_h(n):
    '''Função que dado o valor de N, calcula
    o somatório de H com N '''
    'int---->float'
    soma = [1]
    for numero in range(2, n+1):
        soma.append((numero)**-1)
        somatorio = sum(soma)
        resultado=round(somatorio, n)
    return resultado