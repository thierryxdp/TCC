def retira_pontuacao(frase):
    """retira a pntuação de uma frase; str->str"""
    frase=str.frase
    return frase.maketrans('.', '!', string.punctuation)