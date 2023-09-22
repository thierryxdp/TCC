def conta_frases(texto):
    """ Recebe um texto e retorna o número de frases com base na sua pontuação"""
    var1 = str.count(texto,'.')
    var2 = str.count(texto,'…')
    var3 = str.count(texto,'?')
    var4 = str.count(texto,'!')
    var5 = var1 + var2 + var3 + var4 
    return var5