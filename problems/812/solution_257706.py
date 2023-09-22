def retira_pontuacao(frase):
    """retira a pntuação de uma frase; str->str"""
    return frase.maketrans('.', '!', string.punctuation)