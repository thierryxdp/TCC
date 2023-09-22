def retira_pontuacao(frase1):
    """função que retira a pontuação de uma frase.
    str -> str"""
    for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase1, ponto , " ")
    return frase1

def inverte (frase):
    """função que dada uma frase inverte a ordem das palavras da frase.
    str -> str"""
    lista = str.split(frase1)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase1