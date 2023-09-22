def primo(n):
    '''Uma função que ao recebe um numero retorna se é primo
    ou não int ->booleano'''
    soma=0
    for i in range(2,n):
        if n%i == 0:
            soma=+1 
    if soma==1:
        return True           
    else:
        return False