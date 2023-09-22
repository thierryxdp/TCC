def primo(numero):
    '''Coloque um numero e o resultado será se ele é primo ou não
       int->bool'''
    contador=0
    for i in range(numero):
        if numero%(i+1)==0:
            contador=contador+1
    if contador==2:
        return True
    else:
        return False