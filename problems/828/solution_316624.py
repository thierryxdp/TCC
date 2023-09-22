def primo(numero):
    '''Rece um número e verifica se ele é primo ou não
    int -> bool'''
    
    for i in range(0,numero+1):
        if i % i != 0:
            if numero % i != 0:
                return True
            else:
                return False