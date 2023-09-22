def primo(n):
    '''retorna se o numero inteiro e positivo n e primo ou nao;
    0<int->bool'''
    for i in range(2,n):
        if n%i == 0:
            return False
    return True