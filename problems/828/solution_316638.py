def primo(numero):
    '''Rece um número e verifica se ele é primo ou não
    int -> bool'''
   
    
    for i in range(1,numero+1):
        if numero % i or numero % numero != 0:
            return True
        else:
            return False