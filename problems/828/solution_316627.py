def primo(numero):
    '''Rece um número e verifica se ele é primo ou não
    int -> bool'''
    primos = []
    
    for i in range(1,numero+1):
        if i % i !== 0:
            primos += [i]
    return primos