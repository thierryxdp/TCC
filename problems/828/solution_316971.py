def primo(numero):
    '''
    dado um numero inteiro positivo como argumento,
    retorna o bool 'True' se for primo e o bool 'False'
    se for não o for
    dados de entrada: int
    retorna: bool
    '''
    primos = [2,3,5,7,11,13,17,19,23,29,31,37,41,43,47]
    if numero <= primos[-1]:
        if numero in primos:
            return True
        else:
            return False
    if numero > primos[-1]:
        for i in primos:
            if (numero % i) == 0:
                return False
        else:
            for i in range(primos[-1],n):
                if (numero % n) == 0:
                    return False
                else:
                    return True