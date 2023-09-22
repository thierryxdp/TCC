def primo(n):
    """Esta é a função  que dado um número inteiro positivo retorna se ele é primo ou não, int -> bool"""

    for x in range(2, n ):
        if n % x == 0:

            return False

        else:

            return True