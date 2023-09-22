def primo(n):
    '''essa funçao verifica se um numero inteiro e primo ou nao
    int-> int'''
    a=0
    i=0
    for i in range(1, n+1):
        if n%i==0:
            a=a+1
     
        elif a==1  or a>2:
            return False
        else:
            return True