def primo(numero):
    '''recebe um numero e retorna se ele é primo ou não'''
    cont = 0
    i = 0
    
    while i <= numero or cont < 2:
        i = i + 1
        x = numero % i
        if x == 0:
            cont = cont + 1
        if cont <= 2:
            return True
        else:
            return False