def retira_pontuacao(frase):
    """retira a pntuação de uma frase; str->str"""
    frase=frase
    return frase.maketrans('.', '!', string.punctuation)