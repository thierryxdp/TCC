def retira_pontuacao(frase):
    """."""
    caracteres = "–",",",":",".",";",":","?","!"
    if caracteres in frase:
        return str.replace(frase, caracteres, " ")