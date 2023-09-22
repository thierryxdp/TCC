def primo(n):
    '''função que, dado um número inteiro positivo, retorna se o número
    é primo ou não'''
    divisores = []
    for x in range(2,n):
        if n % x == 0:
            list.append(divisores,x)
    if len(divisores) == 0:
        return True
    else:
        return False