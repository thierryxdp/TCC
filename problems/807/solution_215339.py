def conta_frases(texto):
    '''retorna o numero de frases em um texto, 
    assumindo ., ..., ! e ? como pontos finais; str -> int'''
    t = str.replace(texto,'...','@')
    return str.count(t,'@')+str.count(t,'.')+str.count(t,'!')+str.count(t,'?')