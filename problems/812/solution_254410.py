def retira_pontuação(frase):
    """função que retira a pontuação das frases"""
    frase.replace("!","#")
    frase.replace(",","#")
    c=str.replace("#","")
    return c