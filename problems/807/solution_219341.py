def conta_frases(texto):
    '''função que dado um texto retorna a quantidade 
    de frases contidas nele'''

    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')