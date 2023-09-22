def primo(numero):
    '''funcao que recebe um numero e verifica se ele é primo ou não, retornando um booleano.
    int -> bool
    Explicação: sabida q quantidade de divisores, se ela for igual a 2, o número 
    será primo, excetuando o numero 1 que possui apenas 1 divisor.'''
    div=[]
    for c in range(1,numero+1):
        if numero%c==0:
            div=(div+[c])
    if len(div)==2:
        return True
    else: 
        return False