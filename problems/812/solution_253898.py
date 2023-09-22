def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    if '-' in frase:
        s = str.replace(frase, '-', ' ')
        return s.replace('.', ' ')
    elif '?' in frase:
        d = str.replace(frase, '?', ' ')
        return d.replace(',', ' ')
    elif '.' in frase:
        p = str.replace(frase, '.', ' ')
        return p.replace(',', ' ')