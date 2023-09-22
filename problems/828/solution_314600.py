def primo(numero):
    '''retorna se o número é primo ou não.
    int -> bool'''
    soma = 0
    for i in range(1, numero):
        if numero % i == 0:
            soma = soma + 1
    return soma == 1