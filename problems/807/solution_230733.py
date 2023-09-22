def conta_frases (texto):
    '''função em que dado um texto retorne o múmero de frase que constam no
    texto informado (considerando que todas as frases terminem com uma das
    seguintes pontuações '!', '?', '.' ou '...');
    str -> int'''
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    ponto=(str.count(texto,'.'))%((str.count(texto,'...'))*3)
    reticencias=str.count(texto,'...')
    return exclamacao+interrogacao+ponto+reticencias