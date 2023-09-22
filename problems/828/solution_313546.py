def primo(n):
    '''Funcao que dada um numero inteiro e positivo n retorna True
    se o mesmo for primo e False no caso contrario'''
	quantidade=0
    for numero in range(1,n+1):
        if n%numero==0:
            quantidade=quantidade+1
        if quantidade>1:
            return True
        elif quantidade<=1:
            return False