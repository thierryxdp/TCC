def primo(n):
    """funcao que retorna se o numero n e prrimo ou nao;
    int -> bool"""

    lista = list(range(1,n+1))
    b = bool()

    for termo in lista:

        if n % termo != 0:
            b == True

        else:
            b == False

    return b