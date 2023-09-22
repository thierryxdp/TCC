def fatorial(n):
    '''
    Esta função recebe um número inteiro e retorna um número inteiro representando o fatorial do número fornecido
    
    Parametros
    ----------
    n (int) : número
    '''
    f = n
    while n > 1:
        f = f*(n - 1)
        n = n - 1
    return f