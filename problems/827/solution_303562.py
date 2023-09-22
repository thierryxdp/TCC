def qtd_divisores(n):
    '''função que conta o números de divisores positivos que o número de entrada n tem'''
    m = []
    if n == 0:
        return "Todos os números são divisores de zero, exceto o próprio zero"
    if n < 0:
        n = -n
    for i in range(1,n+1):
        if n % i == 0:
            m += [i]
    return len(m)