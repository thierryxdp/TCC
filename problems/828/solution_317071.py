def primo(n):
    '''essa funcao analisa se um numero n é primo ou nao, baseado
    na quantidade de divisores que ele possui
    int -> bool'''
    cont=0
    for i in range(1,n+1):
        if n%i==0:
            cont=cont+1
    if cont<=2:
        return True
    else:
        return False