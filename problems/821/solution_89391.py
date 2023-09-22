def fatorial(n):
    ''' dado um numero n de entrada ira calcular o fatorial desse numero, int => int '''
    i = 0
    factorial = 1
    while 1<=n:
        factorial = factorial*n
        n = n - 1
        i =i + 1
    return factorial