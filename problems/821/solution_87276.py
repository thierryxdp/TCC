def fatorial(num):


    """Função que recebe um número e retorna o fatorial."""
    #int -> int: 5 -> 120

    c = cont = 1

    while cont < num:
        cont += 1
        c *= cont

    return c