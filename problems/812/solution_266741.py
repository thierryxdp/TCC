def retira_pontuacao(frase):
    """."""
    caracteres = "–",",",":",".",";","?","!"
    if "–" in frase:
        str.replace(frase, "–", " ")
    if "," in frase:
        str.replace(frase, ",", " ")
    if ":" in frase:
        str.replace(frase, ":", " ")
    if "." in frase:
        str.replace(frase, ".", " ") 
    if ";" in frase:
        str.replace(frase, ";", " ")
    if "?" in frase:
        str.replace(frase, "?", " ")
    if "!" in frase:
        str.replace(frase, "!", " ")
    return frase