def conta_frases(texto):
    '''
    Funçao que recebe um texto e conta o numero de frases que tem
    nele de acordo com a pontuaçao
    str -> int
    '''
    e=str.replace(texto,'!','.')
    i=str.replace(e,'?','.')
    r=str.replace(i,'...','.')
    
    return str.count(r,'.')