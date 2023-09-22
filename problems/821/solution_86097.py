def fatorial(n:int)->int:

    """ Função que dado um número n, calcula e retorna seu fatorial """

    x = n

    fatorial = n


    if n == 0:

        return 1

    else:

        while x > 1:

            x = x - 1
            fatorial = fatorial * x

        return fatorial