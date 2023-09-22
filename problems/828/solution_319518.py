def primo(numero):

    contador = 1

    divisores = 0

    while numero > contador:

        if divisores >= 3:

            return False

        if numero % contador == 0:

            divisores += 1

            contador += 1

        else:

            contador += 1

    else:

        return True