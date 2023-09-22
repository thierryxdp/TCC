def conta_frases(texto):
    """Função que retona uma frase ate seu caractere"""
    if (texto, "."):
        return str.count(texto, ".")
    elif (texto, "!"):
        return str.count(texto, "!")
    elif (texto, "?"):
        return str.count(texto, "?")
    else:
        return 1
    return str.split(texto)