def retira_pontuação:
    """função que retira a pontuação das frases"""
    str.replace("!","#")
    str.replace(",","#")
    c=str.replace("#","")
    return c