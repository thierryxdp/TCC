def retira_pontuacao(frase):
    """Função que retira a pontuação de uma frase e a substituí por espaços. tr -> str"""
    if "." in frase:
        frase = frase.replace("."," ")
    if "!" in frase:
        frase = frase.replace("!"," ")
    if "?" in frase:
        frase = frase.replace("?"," ")
    if "..." in frase:
        frase = frase.replace("..."," ")
    if "," in frase:
        frase = frase.replace(","," ")
    if "-" in frase:
        frase = frase.replace("-"," ")
    return frase

def inverte(frase):
    """Função que remove a pontuação de uma frase e a inverte. str -> str"""
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)