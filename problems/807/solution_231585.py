def conta_frases (texto):
    '''Função que retorna o número de frases, dado um texto, que constam no
    texto informado (considerando que todas as frases terminem com uma das
    seguintes pontuações '!', '?', '.' ou '...');
    str -> int'''
    exclamacao=str.count(texto,'!')
    interrogacao=str.count(texto,'?')
    ponto=(str.count(texto,'.'))-((str.count(texto,'...'))*3)
    reticencias=str.count(texto,'...')
    return exclamacao+interrogacao+ponto+reticencias