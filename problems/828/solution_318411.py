def primo(x):
    """ Função que, dado um n° inteiro, verifique se o mesmo é 
    primo ou não, e retorne um valor booleano; int=>bool"""
    n = 0
    for y in range(1, x + 1):
        if x % y == 0:
            n += 1

    if n == 2:
        return True
    else:
        return False