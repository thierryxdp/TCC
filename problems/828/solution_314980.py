def primo(numero):
    '''dado um numero inteiro positivo retoma um valor boleano'''
    contador=0
    for i in range(1,numero+1):
        if numero%i==0:
            contador = contador+1
    if contador ==2:
        return True 
    else:
        return False