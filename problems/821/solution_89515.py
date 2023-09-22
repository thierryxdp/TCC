def fatorial(numero):
    """
    Funçao que recebe um número e retorna o fatorial desse mesmo número.
    """
    contador = 1
    fatorial = 1

    while contador <= numero:
        fatorial *= contador
        contador += 1
       
    return fatorial