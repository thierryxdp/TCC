def inverte(texto):
    """Dado um texto inverte a ordem das palavras
    str --> str"""
    b = str.lower(retira_pontuacao(texto))
    c = str.split(b)[::-1]
    d = str.join(' ',c)
    return b