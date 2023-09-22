def primo(n):
    """ verifica se o número inteiro e positivo dado é ou não um
    número primo"""
    if n == 1:
        return False
    x = 0 
    for y in range(2,n):
        if (n % y == 0):
            x+=1
    if x == 0:
        return True
    else:
        return False