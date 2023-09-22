def conta_frases(frases: str) -> int:
    """dhjgdfjg"""
    
    retira_ponto = frases.split(".")
    retira_excla = retira_ponto.split("!")
    retira_inter = retira_excla.split("?")
    retira_reticen = retira_inter.split("...")
    
    conta_frases = len(retira_reticen)
    return conta_frases