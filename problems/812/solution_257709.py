def retira_pontuacao(frase):
    """retira a pntuação de uma frase; str->str"""
    frase=frase
    novafrase=frase.translate(str.maketrans(' ', ' ', string.punctuation))
    return (novafrase)