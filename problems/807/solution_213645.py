def conta_frases(frase):
    """Conta o numero de frases que aparcem nesse texto.
    ent-> str
    saida-> int"""

    frase=str.replace(str.replace(str.replace(str.replace(frase,'...', '#'),'!', '#'),'.', '#'),'?', '#')
    return frase.count("#")