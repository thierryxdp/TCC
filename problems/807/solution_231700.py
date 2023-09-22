def conta_frases(texto):
    '''funcao que retorna o numero de frases que terminam em '.', '!', '?','...' em um certo texto str->int'''
    ponto_exclamacao = str.count(texto,'!')
    ponto_interrogacao = str.count(texto,'?')
    tres_pontos = str.count(texto,'...')
    #ponto = str.count(texto,'.')-((str.count(texto,'...'))#*3  
    ponto = str.count(texto,'.')-(str.count(texto,'...')*3
    return ponto_exclamacao + ponto + ponto_interrogacao + tres_pontos