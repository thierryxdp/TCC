def primo(n):
    """função que recebe um número inteiro n e retorna True
    se esse número for primo, se o número não for primo ela 
    retorna False.
    int -> bool"""
    intervalo = range(2,n)
    divisores = []

    for numero in intervalo:
        if n % numero == 0:
            divisores += [numero]
    if sum(divisores) == 0:
        return True
    else:
        return False