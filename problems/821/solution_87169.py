'''Recebe um numero positivo e retorna o seu fatorial'''
#int -> int
def fatorial(numero):
    factorial = 1
    contador = 1
    while contador < numero:
        if contador == 1:
            factorial = numero*(numero - contador)
        else:
            factorial = factorial*(numero - contador)
        contador = contador + 1
    if numero < 0:
        return 'O numero de entrada deve ser positivo !'
    else:
        return factorial