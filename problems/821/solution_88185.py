def fatorial(numero):
    while numero > 0:
        fat = 1
        while numero > 1:
            fat = fat  * numero
            numero = numero - 1
            return fat