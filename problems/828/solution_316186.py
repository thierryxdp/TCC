def primo(a): 
    '''Esta e a funcao que dado um numero inteiro positivo,
    verifica-se se este numero e primo ou nao, 
    retornando um valor booleano'''
    x = True 
    for i in range(2, a): 
        if a%i == 0: 
            x = False
    return x