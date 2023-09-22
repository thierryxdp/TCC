def primos(numero):
    '''função que verifica se um número é primo;
       int => bool'''
    contador = 0
    for i in range(2,numero):
        if numero % i == 0:
            contador = contador+1
    if contador > 0:
        return False
    else:
        return True