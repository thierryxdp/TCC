def primo(numero):
    '''Determina se um número é primo ou não
    entrada:int
    saída:int
    '''
    numerodivisores=0
    for divisor in range(1,numero+1):
        if numero%divisor==0:
            numerodivisores=numerodivisores+1
    if numerodivisores==1:
        return True
    else:
        return False