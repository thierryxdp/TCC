def conta_frases(texto):
    """ Recebe um texto e retorna o número de frases com base na sua pontuação"""
    var1 = str.count(texto,'.')
    var2 = str.count(texto,'...')
    var3 = str.count(texto,'?')
    var4 = str.count(texto,'!')
    if var2 == 0: 
        return var1 + var3 + var4 
    elif var2 > 0:
        return var2 + var3 + var4 + var1 - (3*var2)