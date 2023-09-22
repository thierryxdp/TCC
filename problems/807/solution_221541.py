def conta_frases(texto):

    x = str.count(texto,".")

    y = str.count(texto,'!')
    
    z = str.count(texto,'...')
    
    k = str.count(texto,'?')

    l = (str.count(texto,"..."))*3

    f = x + y + z + k - l

    return f