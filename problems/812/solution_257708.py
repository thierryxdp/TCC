def retira_pontuacao(frase):
    """retira a pntuação de uma frase; str->str"""
    return str.maketrans(' ', ' ', string.punctuation)