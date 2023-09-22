def inverte(frase):
    """Dada uma frase, retorna a frase sem os caracteres de pontuação"""
    texto=str.replace(frase, ",", "")
    texto=str.replace(texto, "-", " ")
    texto=str.replace(texto, ".", "")
    texto=str.replace(texto, ":", "")
    texto=str.replace(texto,";", "")
    texto=str.replace(texto, "!", "")
    texto=str.replace(texto, "?", "")
    texto=str.lower(texto)
    separar=str.split(texto, " ")
    inverter=separar[: :-1]
    frase_invertida=str.join(" ", inverter)
    return frase_invertida