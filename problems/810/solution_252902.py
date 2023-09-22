def retira_pontuacao(frase):
    """função que retira a pontuação de uma frase.
    str -> str"""
    for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase, ponto , " ")
    return frase

def inverte (frase):
    """função que dada uma frase inverte a ordem das palavras da frase.
    str -> str"""
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    frase = str.replace(frase, ".", ",", " ")
    return frase