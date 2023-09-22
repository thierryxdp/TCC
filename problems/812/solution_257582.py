def retira_pontuacao(frase):
    """ Essa função retira a pontuação da frase introduzida e retorna-a. str->str"""
    frase = frase.replace("." and "," and "?" and "-" and "!", " ")
    return frase