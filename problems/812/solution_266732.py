def retira_pontuacao(frase):
    """."""
    caracteres = "–,:.;:?!"
    for c in caracteres:
        frase = text.replace(c, " " + c)
        return frase