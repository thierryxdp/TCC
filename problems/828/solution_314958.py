def primo(p):
    '''Função que verifica se um número inteiro e positivo é ou não primo.'''
    d=()
    for n in range(1,p+1):
        if p%n==0:
            d+=(n,)
    if len(d)<=2:
        return True
    else:
        return False