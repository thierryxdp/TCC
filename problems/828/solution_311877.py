def primo(numero):
    """ essa funçao avalia se o numero inteiro inserido é um numero primo"""
    mult=0
    for i in range(1,numero):
        if numero % i ==0:
            mult+=1
            if mult==1:
                return True
            else:
                return False