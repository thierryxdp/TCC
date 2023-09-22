def lingua_p(palavra):
    """função que dada uma palavra, retorne a mesma traduzida para a lingua do P;str-->str"""
    X=""
    for letra in palavra:
        if letra= "aeiou":
            X+=letra+"p"+letra
        else:
            X+=letra
    return X