def primo(numero):
    '''funcao dado um numero retorna se é um numero primo
    int -> bool'''
    contador = 1

    divisores = 0

    while numero >= contador:




        if numero % contador == 0:

            divisores += 1

            contador += 1

        else:

            contador += 1
    if divisores >= 3:
        return False
    else:

        return True