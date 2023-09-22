import re
def retira_pontuacao(frase):
    """retira a pontuação da frase"""
    out = re.sub(r'[^\w\s]','',frase)
    return out