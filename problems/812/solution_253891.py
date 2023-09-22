def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    s = str.split(frase, ',.;:-?!')
    return s