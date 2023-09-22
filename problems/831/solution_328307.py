def lingua_p(palavra):
    """função que dada uma palavra, retorne a mesma traduzida para a lingua do P;str-->str"""
    X=""
    vogal='aeiouáéíóú'
    for letra in palavra:
        if letra in vogal:
            X+=letra+"p"+letra
        else:
            X+=letra
    return str.lower(X)