def retira_pontuacao(frase):
    """."""
    caracteres = "–",",",":",".",";",":","?","!"
    if caracteres is in frase:
        return str.replace(frase, caracteres, " ")