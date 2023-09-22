def primo(num):
    '''
        funcao chamada primo que dado um numero inteiro positivo,
        verifique se este numero e primo ou nao.
        num:int
        retrun bool
    '''
    
    for i in range(2, num//2+1):    
        if num % i  == 0:
            return False
    return True