def primo(p):
    """ dado um numero p, verifica se é primo ou nao
    int -> bool
    """
    lista = []
    for i in range(1, p + 1):
        if p % i == 0:
            lista.append(i)
    if len(lista) == 2:
        return True
    else:
        return False