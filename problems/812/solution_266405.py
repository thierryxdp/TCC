def retira_pontuacao(frase):
    """retira a pontuação da frase"""
    tirador_de_pontuacao = frase.translate(str.maketrans('','',str.punctuation))
    return tirador_de_pontuacao