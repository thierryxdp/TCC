def lingua_p(palavra):
    """Recebe uma palavra e retorna a mesma traduzida para a língua do P"""
    letra = tuple(palavra)
    for letra in palavra:
        if letra in "aeiouAEIOU":
            palavra = "p" + letra + "p"
    return palavra