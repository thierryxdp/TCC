import string

def retira_pontuacao(frase):
    """Esta função retorna o número de palavras contidas na frase.
       String --> int"""
    
    for c in "!@#$%*()<>:|/?":
    return frase.replace(c, " ")