def inverte(frase):
    """Essa função recebe uma frase, remove sua pontação e a inverte
    str -> str"""
    frase = retira_ponto()
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    retira_ponto = " "
    return(frase)