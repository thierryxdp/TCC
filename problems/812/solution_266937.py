def retira_pontuacao(frase):
    """função que retira a pontuação de uma frase.
    str -> str"""
    for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase, ponto , " ")
    return frase