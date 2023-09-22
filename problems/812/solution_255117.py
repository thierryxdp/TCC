def retira_pontuacao (frase):
    """Função que dada uma frase, a retorne sem as pontuações e com um espaço no lugar"""
    return "".join([char if char in ".!?," else "" for char in frase)