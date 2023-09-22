def conta_frases(texto):
    """Funcao que recebe um texto como entrada, e retorna a quantidade de frases
    string->int"""
    caractere1 = texto.count('!')
    caractere2 = texto.count('?')
    caractere3 = str.count(str.replace(texto,'...','.'),'.')
    return caractere1 + caractere2 + caractere3