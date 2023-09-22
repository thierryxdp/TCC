def conta_frases(texto):

    """Retorna a quantidade de frases que um texto possui dado um texto
assiantura: str--> int

conta_frases("é.é.é.é.é.é.é.")==7"""
    
    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')