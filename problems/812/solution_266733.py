def retira_pontuacao(frase):
    """."""
    caracteres = "–,:.;:?!"
    for c in caracteres:
        frase = str.replace(c, " " + c)
        return frase