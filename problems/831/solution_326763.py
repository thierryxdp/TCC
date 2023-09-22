def lingua_p(palavra):
    """..."""
    contador = 0
    for letra in palavra:
        if letra in 'aeiou':
            palavra[contador:contador] = 'p'+ letra
        contador = contador + 1
    return palavra_nova