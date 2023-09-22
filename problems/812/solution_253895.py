def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    if '-' in frase:
        s = str.replace(frase, '-', ' ')
        return s.replace('.', ' ')