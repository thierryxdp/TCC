def fatorial (numero):
    """Função que retorn a fatorial de um número recebido
    int -> int"""
    if numero < 0:
        return 0
    elif numero == 0:
        return 1
    elif numero == 1:
        return 1
    else:
        fatorial = 1
        while(numero > 1):
            fatorial *= numero
            numero = numero - 1
        return fatorial