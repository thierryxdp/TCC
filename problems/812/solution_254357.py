def retira_pontuacao(frase):
    import re
    novafrase = re.sub(r'[^\w\s]','',frase)
    return novafrase