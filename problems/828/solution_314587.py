def primo(numero):
    '''retorna se o número é primo ou não.
    int -> bool'''
    for i in range(2,numero):
        if i // numero:
            primo = False
        else:
            primo = True
    return primo