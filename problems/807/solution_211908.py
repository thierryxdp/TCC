def conta_frases(f):
    '''recebe um texto e conta o número de frases nele existentes'''
    texto_pontos =str.replace(str.replace(str.replace(f,'!','.'),'?','.'),'...','.')
    conta_pontos =str.count(texto_pontos,'.')
    return conta_pontos