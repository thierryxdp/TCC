def primo(numero):
    """A função recebe um número inteiro positivo (int)
    e retorna um booleano indicando se o número é primo
    (True caso seja e False caso não seja)."""
    lista = list(range(numero))
    del(lista[0])
    del(lista[0])
    for elemento in lista:
        if numero % elemento == 0:
    return False
        else:
            return True