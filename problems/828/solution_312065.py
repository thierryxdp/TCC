def primo(numero):
    '''Calcula e retora se um numero é ou nao primo
       parameters:
       numero: numero positivo e inteiro qualquer
       int-> int'''
    proximo=2
    for proximo in range(1,numero):
        if numero%proximo==0:
            proximo +=1
            return False
        else:
            proximo +=1
            return True