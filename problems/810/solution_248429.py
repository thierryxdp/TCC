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

def inverte(frase):
    frase = frase.lower()
    frase = retira_pontuacao(frase)
    frase = frase.split(" ")
    frase = frase[::-1]
    frase = ' '.join(frase)
    return frase