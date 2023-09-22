def primo(n):
    '''Retorna se o número de entrada é primo'''
    resposta=0
    for divisor in range(n+1):
        if divisor!=0 and n%divisor==0:
            resposta=resposta+1
    if resposta==2:
        return True
    else:
        return False