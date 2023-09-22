def conta_frases(texto):
    ''' funcao que calcula e retonra o numero de frases que aparecem em um texto '''
    ''' str -> int '''
    x = ','
    y = '.'
    z = '!'
    list = (x, y, z,)
    var1 = str.split(texto)
    var2 = var1.replace(list)
    var3 = len(var2)
    return var3