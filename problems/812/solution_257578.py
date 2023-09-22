def retira_pontuacao(frase):
    """ Essa função substitui cada pontuação existem por espaços em branco"""
    frase = frase.split(",")
    frase = frase.split(".")
    
    return frase