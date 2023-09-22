def primo(n):
    '''verifique se um numero e primo e retorne com um valor booleano
    :param n: int->int
    :return: bool->bool
    '''
    numerosprimos = 0
    for i in range(1, n + 1):
        if n % i ==0:
            numerosprimos +=1
            
    if numerosprimos ==2:
        return True
    else:
        return False