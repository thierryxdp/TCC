def inverte(frase):
    """xxxxx"""
    frase=frases.replace(',', '')
    lista_ponc=set('-.:;!?/,#$@&)('"')
    frasessemp = ''.join(i if i not in lista_ponc else ' ' for i in frase)).lowe
    palavras=frasessemp.split(' ')
    r= ' '.join(reversed(palavras))
    return r[1:]