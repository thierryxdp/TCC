def primo(n):
    """funcao que retorna se o numero n e prrimo ou nao;
    int -> bool"""

    divisores = []

    for termo in range(1,n+1):

        if n % termo == 0:

            divisores.append(termo)

    if len(divisores) == 2:
        return True

    else:
        return False