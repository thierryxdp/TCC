def conta_frases(x):
    '''funcao que retorna o numero de frases, de acordo
    com o numero de pontuacoes'''
    x=str.replace(x,'!','.')
    x=str.replace(x,'?','.')
    x=str.replace(x,'...','.') 
    return str.count(x,'.')