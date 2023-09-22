def qtd_divisores(numero):
    '''Coloque um numeo e o resultado será o número de divisores dele
       int->int'''
    contador=0
    for i in range(numero):
        if numero%(i+1)==0:
            contador=contador+1
    return contador