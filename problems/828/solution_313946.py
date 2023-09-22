def primo(n):
    '''verifica se o numero e primo ou nao;
    entrada:int
    saida:int'''
    if n==1:
        return False
    for i in range(2,n//2+1):
        if n%i==0:
            return False
    return True