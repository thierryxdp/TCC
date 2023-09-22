def conta_frases(texto):
    '''retorna o numero de frases em um texto, 
    assumindo ., ..., ! e ? como pontos finais; str -> int'''
    texto.replace('...','@')=t
    return t.count('@')+t.count('.')+t.count('!')+t.count('?')