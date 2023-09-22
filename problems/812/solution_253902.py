def retira_pontuacao(frase):
    """Dada uma frase, retorna a mesma frase só que sem pontuação; string->string"""
    if '!' in frase:
        s = str.replace(frase, '-', ' ')
        p = s.replace(',', ' ')
        d = p.replace(':', ' ')
        f = d.replace(';', ' ')
        return f.replace('!', ' ')
    elif '?' in frase:
        g = str.replace(frase, '-', ' ')
        h = s.replace(',', ' ')
        i = p.replace(':', ' ')
        j = d.replace(';', ' ')
        return f.replace('?', ' ')
    elif '.' in frase:
        k = str.replace(frase, '-', ' ')
        l = s.replace(',', ' ')
        m = p.replace(':', ' ')
        n = d.replace(';', ' ')
        return f.replace('?', ' ')