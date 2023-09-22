def conta_frases(frase):
    '''Essa função toma o texto inserido e retorna o número de frases contidas no texto de acordo com a pontuação;
    STRING -> INT'''
    if '...' in frase:
        return (str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+str.count(frase,'...'))-3*str.count(frase,'...')
    else:
        return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+str.count(frase,'...')