def retira_pontuacao(frase):
    """ Essa função retira a pontuação da frase introduzida e retorna-a. str->str"""
    frase = str.strip(frase, "!?,-.")
    return frase