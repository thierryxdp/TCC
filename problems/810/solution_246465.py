def inverte(texto):
    """função que inverte uma frase, sem letra maiusculas
    e sem pontuação
    str->str"""
    texto = texto.lower()
    texto = texto.replace("-", " ")
    texto = texto.replace(",", " ")
    texto = texto.replace(":", " ")
    texto = texto.replace(";", " ")
    texto = texto.replace(".", " ")
    texto = texto.replace("!", " ")
    texto = texto.replace("?", " ")
    texto = texto.replace("...", " ")
    texto = texto.split()
    texto.reverse()
    texto = tuple(texto)
    texto = str.join(" ", texto)
    return texto