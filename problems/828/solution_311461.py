def primo(n):
    '''função que dado um número inteiro positivo, retorna True se este número for primo e False se não for'''
    x = []
    for i in range(1,n+1):
        if n % i == 0:
            x += [i]
    if len(x) == 2:
        return True
    else:
        return False