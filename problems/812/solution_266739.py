def retira_pontuacao(frase):
    """."""
    caracteres = "–",",",":",".",";",":","?","!"
    if "–"or","or":"or"."or";"or":"or"?"or"!" in frase:
        return str.replace(frase, ("–",",",":",".",";",":","?","!"), " ")