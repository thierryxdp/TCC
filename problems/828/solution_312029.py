def primo(numero):
    '''Calcula e retorna se um numero estabelecido é ou nao primo, ou seja, nao sera primo se possuir divisores sem ser o 1 ou ele mesmo
       parameters:
       numero: numero inteiro e positivo qualquer
       int->bool'''
    proximo=2
    for proximo in range(2,numero):
        if numero%proximo==0:
            proximo += 1
            return False
        if numero%proximo!=0:
            proximo +=1 
            return True