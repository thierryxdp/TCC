def retira_pontuacao (frase):
    """Função que dada uma frase, a retorne sem as pontuações e com um espaço no lugar"""
    return frase.replace('-', ' ') or frase.replace(',', ' ') or frase.replace(':', ' ') or frase.replace(';', ' ') or frase.replace('.', ' ') or frase.replace('!', ' ') or frase.replace('?', ' ')