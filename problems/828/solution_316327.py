def primo(numero):
    '''Dado um número inteiro positivo, retorna se esse número é primo ou não.
    int-->bool'''
    qdt_div=0
    for n in range(1,numero+1):
        if numero%n==0:
            qdt_div=qdt_div+1
    if qdt_div==2:
        return True
    else:
        return False