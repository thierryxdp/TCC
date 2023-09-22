def primo(numero):
    '''Informa se o número apresentado é ou não um número Primo
int->bool'''
    divisores=0
    numeros_dividir= list(range(2,numero))
    for i in numeros_dividir:
        if numero % i == 0:
            divisores+=1
    if divisores>0:
        return False
    else:
        return True