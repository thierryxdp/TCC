def primo(numero):
    """A função recebe um número inteiro positivo (int)
    e retorna um booleano indicando se o número é primo
    (True caso seja e False caso não seja)."""
    lista = list(range(numero))
    del(lista[0])
    del(lista[0])
    contador = 0
    while numero % lista[contador] != 0:
        contador += 1
        if contador = numero - 4:
            return True
    return False