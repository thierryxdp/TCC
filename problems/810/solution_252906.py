def retira_pontuacao(frase):
    """função que retira a pontuação de uma frase.
    str -> str"""
    for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase, ponto , " ")
    return frase

def inverte (frase):
    """função que dada uma frase inverte a ordem das palavras da frase.
    str -> str"""
    import retira_pontuacao()
    lista = str.split(frase)
    reversed.lista()
    frase = str.join(" ", lista)
    return lower(frase)