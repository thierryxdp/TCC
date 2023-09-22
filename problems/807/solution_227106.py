def conta_frases(texto):
    """A função retorna a quantidade de frases em um determinado texto
    str-->int."""
    frase1 = len(str.split(texto,"."))
    frase2 = len(str.split(texto,"!"))
    frase3 = len(str.split(texto,"?"))
    frase4 = str.count(texto,"...")
    return (frase1  + frase2 + frase3 - 2 * frase4 -3)