def soma_h(n):
    '''
    Esta função recebe um número inteiro e retorna o valor float da soma 1/n + 1/(n-1) + 1/(n-2) +...+ 1, com
    duas casas decimais.
    
    Parametros
    ----------
    n (int) : número inteiro
    '''
    return round(sum([1/i for i in range (1, n)]), 2)