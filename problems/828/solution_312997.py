def primo(n):
    ''' Verifica se o número recebido é primo ou não
    int (+) -> bool'''
    primo = True
    for i in range(2,n):
        if n % i == 0:
            primo = False
    return primo