def primo(numero):
    '''Calcula e retora se um numero é ou nao primo
       parameters:
       numero: numero positivo e inteiro qualquer
       int-> int'''
    divisores=2
    for divisores in range(2,n):
        if numero%divisores==0:
            divisores +=1
            return False
        else:
            return True