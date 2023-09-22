def primo(n):
    '''Funcao que dado um numero inteiro e positivo 'n', retorna se o mesmo
    é primo ou não
    int->bool'''
    for x in range(1,n):
        if n%x!=0:
            return True
        else:
            return False