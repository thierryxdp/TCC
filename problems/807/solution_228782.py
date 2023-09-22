def conta_frases(texto):
    ''' função que conta o número de frases que aparecem
    	em um determinado texto. 
        str ---> int '''
    a = str.count(texto, '.')
    b = str.count(texto, '!')
    c = str.count(texto, '?')
    return a + b + c