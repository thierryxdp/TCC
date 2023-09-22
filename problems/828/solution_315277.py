def primo(numero):
    '''Recebe um numero inteiro positivo e retorna se ele é primo ou nao(True se é, False se não)
    int -> bool'''
    if numero%2==0 and numero!=2:
        return False
    i=3
    while i<numero:
        if numero%i==0:
            return False
        i=i+2
    return True