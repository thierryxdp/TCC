def conta_frases(texto):
    '''retorna o numero de frases em um texto, 
    assumindo ., ..., ! e ? como pontos finais; str -> int'''
   
    return str.count((str.replace(texto,'...','@')),'@')+str.count(texto,'.')+str.count(texto,'!')+str.count(texto,'?')