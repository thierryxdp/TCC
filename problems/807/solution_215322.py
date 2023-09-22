def conta_frases(texto):
    '''retorna o numero de frases em um texto, 
    admitindo ., ..., ! e ? como pontos finais; str -> int'''
    return str.count(str.split(str.split(str.split(str.split(texto,'.'),'...'),'!'),'?')