def primo(n):
    '''Verificacao de um inteiro dado como 
    argumento retorna se o numero é primo ou não.int->bool'''
    for i in range(2,n):
        if n%i==0:
            x = False
        	if n%i!=0:
                x = True
    return True