def primo(numero):
    '''Calcula e retora se um numero é ou nao primo
       parameters:
       numero: numero positivo e inteiro qualquer
       int-> int'''
    for proximo in range(2,numero):
        if numero%proximo==0:
            return False
        else:
            return True