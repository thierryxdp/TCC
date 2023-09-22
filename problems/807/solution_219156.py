def conta_frases(frases: str) -> int:
    """dhjgdfjg"""
    
    retira_ponto = frases.split(".")
    retira_excla = str(retira_ponto).split("!")
    retira_inter = str(retira_excla).split("?")
    retira_reticen = str(retira_inter).split("...")
    
    conta_frase = len(retira_reticen)
    return conta_frase