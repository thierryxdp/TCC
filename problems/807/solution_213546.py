def conta_frases(texto):
    '''funcao que conta o numero de frases dentro de um texto'''
    ''' str -> int '''
    var1 = str.split(texto)
    var2 = str.replace(',' '.' '!')
    var3 = var1 - var2
    var4 = int(input(var3))
    return var4