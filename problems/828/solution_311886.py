def qtd_divisores(n:int)->int:

    """ Função que, dado um número inteiro n, calcula a quantidade de divisores
        desse número.
    """

    qtd_div = 0

    for divisor in range(1,(n+1)):

        if n % divisor == 0:

            qtd_div = qtd_div + 1

    return qtd_div


def primo(n:int)->bool:

    """ Função que retorna a condição,e ele é primo ou não, dado um número inteiro(n) """

    if qtd_divisores(n) == 2:

        return True

    else:
        
        return False