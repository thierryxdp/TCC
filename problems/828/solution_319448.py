def qtd_divisores(n):
    '''funcao que conta aquantidade de divisores de um numero'''
    a=0
    for i in range(1, n+1):
        if n%i==0:
            a+=1
    return a

def primo(numero):
    if qtd_divisores(n)==2:
        return True
    else:
        return False