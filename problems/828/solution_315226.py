def primo(numero):
    '''retorna se o numero é primo ou nao'''
    '''int -> bool'''
    
    if numero >= 2:
        for divisor in range( 2, numero ):
            if not ( numero % divisor ):
                return False
    else:
        if (numero % divisor):
            return True