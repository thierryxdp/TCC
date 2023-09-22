def conta_frases(texto):
    '''insira um texto string, irá retornar a quatidade de frases terminadas por pontos dentro da mesma'''
    return len(str.split(texto,('?' and '...' and '.' and '!'and ',' and ';')))-1