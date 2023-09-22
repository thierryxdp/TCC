def conta_frases(texto):
    '''funcao que conta o numero de frases dentro de um texto'''
    ''' str -> int '''
    var1 = len(texto)
    var2 = str.replace(texto)
    var3 = var1 - var2
    var4 = int(input(var3))
    return var4