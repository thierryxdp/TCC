def inverte(frase):
    """Função que remove a pontuação de uma frase e a inverte. str -> str"""
    frase = retira_pontuacao(frase)
    frase = frase.lower()
    frase = frase.split()
    frase.reverse()
    frase = " ".join(frase)
    return(frase)