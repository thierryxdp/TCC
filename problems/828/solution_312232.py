def primo(numero):
    '''funçao que dado um numero inteiro positivo,
    retorna um valor boolenado indicando se é primo ou nao'''
    divisores = 0
    for c in range(1,numero+1):
        if numero%c == 0:
            divisores +=1
        else:
            pass
    if divisores > 2:
        return False
    else:
        return True