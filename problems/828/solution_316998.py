def primo(n):
    '''
    dado um inteiro n, retorna True se o mesmo for primo e
    False caso o contrario
    dados de entrada: int
    retorna bool
    '''
    primos = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89 , 97]
    if n <= primos[-1]:
        if n in primos:
            return True
        else:
            return False
    elif n > primos[-1]:
        for i in primos:
            if (n % i) == 0:
                return False
        for i in range(primos[-1] + 1, n):
            if (n % i) == 0:
                return False
        else:
            return True