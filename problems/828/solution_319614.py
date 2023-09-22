def primo(n):
    """A função recebe um número inteiro e retorna com um valor booleano
    se esse número é um número primo ou não"""
    r = []
    for i in list(range(1 , n + 1)):
        if n%i == 0:
            r.append(i)
    return len(r) == 2