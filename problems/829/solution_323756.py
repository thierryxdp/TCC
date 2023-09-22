def soma_h(n):
    '''
    A função recebe um número e retorna a soma do inverso dos números
    menos ou iguais ao valor informado.

    int -> float
    '''

    i = 1
    soma = 0
    
    while i <= n:
        soma += (1/i)
        i += 1
        
    return round(soma,2)