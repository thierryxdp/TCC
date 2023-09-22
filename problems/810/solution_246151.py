def inverte(frases):
    """ Dada uma frase retorna uma outra frase que contenha as mesmas palavras da frase de entrada na ordem inversa"""
    frase= frases.replace(',','')
    pontuacao = set('-.;:!?/\\,#@$&)(\'"')
    frasessemp = ''.join(i if i not in pontuacao else ' ' for i in (frase)).lower
    palavras = frasessemp.split(' ')
    r = ' '.join(reversed(palavras))
    return r[1:]