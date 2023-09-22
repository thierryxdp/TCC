def conta_frases(texto):
    '''funçao que retorna o numero de frases em um certo texto str->int'''
    if '...' in "texto":
        return str.count(texto, '...') - 2
    return str.count(texto,'.') and str.count(texto,'!')