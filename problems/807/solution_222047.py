def conta_frases(texto):
    '''funcao que recebe um texto e retorna o numero de frases que compoem esse texto
    str -> int'''
    texto=str.replace(texto,'...','#')
    texto=str.replace(texto,'!','#')
    texto=str.replace(texto,'?','#')
    texto=str.replace(texto,'.','#')
    return len(str.split(texto,'#'))