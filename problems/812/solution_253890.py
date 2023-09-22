def retira_pontuacao(text):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    return "".join([" " if char in "-.!?," else char for char in text])