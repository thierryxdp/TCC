def retira_pontuacao(frase):
    """função que recebe frase e tira as pontuações.
    str--> str"""

    if ":" in frase:
        frase = frase.replace(":", " ")
    if ";" in frase:
        frase = frase.replace(";", " ")
    if "." in frase:
        frase = frase.replace(".", " ")
    if "!" in frase:
        frase = frase.replace("!", " ")
    if "-" in frase:
        frase = frase.replace("-", " ")
    if "," in frase:
        frase = frase.replace(",", " ")
    if "?" in frase:
        frase = frase.replace("?", " ")

    return frase