def inverte (frase):
    """função que dada uma frase inverte a ordem das palavras da frase.
    str -> str"""
    for ponto in [".", ",", "!", ":", ";", "-","?"]:
        frase = str.replace(frase, ponto , " ")
    lista = str.split(frase)
    lista.reverse()
return frase = str.join(" ", lista)