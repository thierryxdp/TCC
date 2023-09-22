def primos(x):
    """A funçao diz se a entrada x é um numero primo ou não, se sim retornara True caso contrario, o retorno seára False
    . int --> bool"""
    contagem = 0
    for i in range(1,x+1):
        if x % i == 0:
            contagem = contagem + 1
    if contagem == 2:
        return True
    else:
        return False