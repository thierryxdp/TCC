def primos(n):
    '''Funcao que verifica se um numero inteiro positivo e primo ou nao.
    int -> bool'''
    
    listaDivisores = []

    for i in range(1, n + 1):
        if n % i == 0:
            list.append(listaDivisores, i)
    
    return len(listaDivisores) <= 2