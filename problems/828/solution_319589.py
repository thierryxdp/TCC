def primo(numero):
    """ Recebe um numero e retorna um valor booleano indicando se o numero é primo ou não"""
    lista=list(range(2,numero))

    for i in lista:
        if numero%i==0:
            return False
    
    return True