def conta_frases(texto):
    '''Função que retorna o número de frases que 
    aparecem neste texto.
    texto=str->int'''
    texto = str.replace(texto,'...','.')
    texto = str.replace(texto,'?','.')
    texto = str.replace(texto,'!','.')
    texto = str.split(texto,'.')
    return len(str.count(texto))