def conta_frases(texto):
    """Funcao que recebe um texto e retorna a quantidade de frases que o texto possui.
    string -> string"""
    return str.count(texto,'.') + str.count(texto,'!') + str.count(texto,'?') - 2 * str.count(texto,'...')