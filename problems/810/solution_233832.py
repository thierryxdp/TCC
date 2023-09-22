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
        h = g.replace(',', ' ')
        i = h.replace(':', ' ')
        j = i.replace(';', ' ')
        return j.replace('?', ' ')
    elif '.' in frase:
        k = str.replace(frase, '-', ' ')
        l = k.replace(',', ' ')
        m = l.replace(':', ' ')
        n = m.replace(';', ' ')
        return n.replace('.', ' ')
def inverte(frase):
    """dada uma frase retorna outra frase que conenha as mesmas palavras na ordem inversa se letras maiusculas e sem pontuação; string-> string"""
    n = retira_pontuacao(frase)
    lista = str.split(n)
    invert = lista[::-1]
    sep = str.lower(str.join(' ', invert))
    return sep