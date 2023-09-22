def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    if '!' in frase:
        s = str.replace(frase, '-', ' ')
        p = s.replace(',', ' ')
        d = p.replace(':', ' ')
        f = d.replace(';', ' ')
        return f.replace('!', ' ')
    elif '?' in frase:
        d = str.replace(frase, '?', ' ')
        return d.replace(',', ' ')
    elif '.' in frase:
        p = str.replace(frase, '.', ' ')
        return p.replace(',', ' ')