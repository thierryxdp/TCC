def conta_frases(texto):
    '''
    Funçao que recebe um texto e conta o numero de frases que
    aparecem dentro dele, levando em consideraçao a pontuaçao
    str -> int
    '''
    exclama=str.replace(texto,'!','.')
    pergunta=str.replace(texto,'?','.')
    reticente=str.replace(texto,'...','.')
    quant= exclama + pergunta + reticente
    return str.count(quant,'.')