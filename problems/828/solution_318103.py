def primo(numero):

    """Dado um número inteiro positivo, verifica se ele é primo ou não

    int -> bool"""

    verificador = 0

    for x in range(2, numero):

        if numero%x == 0:

            verificador = 1

    if verificador == 1:

        return False

    if verificador == 0:

        return True