def conta_frases(texto):
    ''' funcao que calcula e retonra o numero de frases que aparecem em um texto '''
    ''' str -> int '''
    x = ','
    y = '.'
    z = '!'
    a = '?'
    b = ':'
    c = ';'
    var1 = str.split(texto)
    var2 = var1.replace(x,y,z,a,b,c)
    var3 = len(var2)
    return var3