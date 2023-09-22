# string -> int
def conta_frase(frase):
    '''Essa função toma o texto inserido e retorna o número de frases contidas no texto de acordo com a pontuação;
    STRING -> INT'''
    return str.count(frase,'.')+str.count(frase,'!')+str.count(frase,'?')+str.count(frase,'...')