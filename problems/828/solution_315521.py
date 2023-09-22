def primo(n):
    '''Uma função que ao recebe um numero retorna se é primo
    ou não int ->booleano'''
    soma=0
    for i in range(1,n+1):
        if n % i == 0:
            soma+=1
            if soma > 2:
                return True
            else:
                return False