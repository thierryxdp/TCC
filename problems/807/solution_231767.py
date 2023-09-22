def quant_palavras(frase):
    """ Recebe uma frase e retorna o número de palavras da frase"""
    var1 = str.count(texto,'.')
    var2 = str.count(texto,'...')
    var3 = str.count(texto,'?')
    var4 = str.count(texto,'!')
    var5 = var1 + var2 + var3 + var4 
    return var5