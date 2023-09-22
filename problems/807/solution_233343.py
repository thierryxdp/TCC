def conta_frases(texto):
    """função que define o número de frases que aparecem em um texto."""
    a = ('.')
    b = ('!')
    c = ('?')
    d = ('...')
    quantidade_de_frases = str.count(texto,a) + str.count(texto,b) + str.count(texto,c) + str.count(texto,d) - 3*str.count(texto,d)
    return quantidade_de_frases