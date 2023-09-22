def retira_pontuacao(frase):
    """xxxxx"""
    frases=frases.replace(',', '')
    lista_pont=set('-.:;!?/,#$@&)('"')
    frasessemp=''.join(i if i not in lista_pont else ' ' for i in frase)).lowe
    palavras=frasessemp.split(' ')
    r= ' '.join(reversed(palavras))
    return r[1:]