def soma_h(n):
    '''
    Dado um numero inteir, a função
    calcula e retorna o valor
    H com n termos e retorna o resultado com 
    2 casa decimais. 
    int --> float.
    '''
    soma = 0
    for x in range(1, n+1):
        soma += 1/x
    return round(soma, 2)