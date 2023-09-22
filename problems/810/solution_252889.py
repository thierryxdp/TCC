def retira_pontuacao(frase1):
    """função que retira a pontuação de uma frase.
    str -> str"""
    for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase, ponto , " ")
    return frase
def inverte (frase1, frase2):
    """função que dada uma frase inverte a ordem das palavras da frase.
    str -> str"""
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase