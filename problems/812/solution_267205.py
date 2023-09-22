def retira_pontuacao(frase):
    """ Função que dada uma frase, retorne a frase sem pontuação  string => string"""
    frase = frase.replace("-", " ")
    frase = frase.replace("!", " ")
    frase = frase.replace(",", " ")
    frase = frase.replace(".", " ")
    frase = frase.replace("?", " ")
    frase = frase.replace(":", " ")
    frase = frase.replace(";", " ")
    return frase