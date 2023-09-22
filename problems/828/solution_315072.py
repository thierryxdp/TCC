def primo(numero):
    '''recebe um numero e retorna se ele é primo ou não'''
    if numero > 1:
        for i in range(2,num):
            if (num % i) == 0:
                return False
            
    else:
        return True