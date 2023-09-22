def primo(numero):
    '''retorna se o número é primo ou não.
    int -> bool'''
    soma = 0
    for i in range(1, numero):
        if i % numero == 0:
            soma += 1
    return soma == 1