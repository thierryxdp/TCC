def conta_frases(texto):
    '''Função que dado um texto, retorna o número de frases que aparecem nesse texto: string -> int'''
    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') + str.count(texto,'...')