def conta_frases(texto):
    '''Função que dado um texto armazenado em uma string, conta o número de frases que aparecem nesse texto: string -> int'''
    return len(str.split(texto,'.') + len(str.split(texto,'!') + len(str.split(texto,'?') + len(str.split(texto,'...')