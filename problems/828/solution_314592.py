def primo(numero):
    '''retorna se o número é primo ou não.
    int -> bool'''
    soma = 0
    for i in range(numero):
        if i // numero:
            soma += i
        else:
            soma += i
    return soma < numero + 1