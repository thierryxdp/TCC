def freq_palavras(frase):
    """
    função que extrai repetições de uma frase e as espelha em um dicionário
    str -> dict
    """

    x = frase.split()
    thing = {i:x.count(i) for i in x}
    return thing