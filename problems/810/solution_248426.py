def retira_pontuacao(frase):
    """Função que dada uma frase retorne uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa, sem letras maiúsculas, e sem a pontuação.string => string"""
    frase = frase.replace("-", " ")
    frase = frase.replace("!", "")
    frase = frase.replace(",", "")
    frase = frase.replace(".", "")
    frase = frase.replace("?", "")
    frase = frase.replace(":", "")
    frase = frase.replace(";", "")
    return frase