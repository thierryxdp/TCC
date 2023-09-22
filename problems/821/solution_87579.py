def fatorial(numero):
    '''Recebe um numero e retorna sua fatorial
    int-->int'''
    resultado=1
    num=1
    while num <= numero:
        resultado = resultado * num
        num = num + 1
    return(resultado)