def conta_frases(numfrases):
    """ função que calcula os numeros das freses apresentado 
    """
    
    b = str.join('.',str.split(numfrases, '...')
    c = str.join('.',str.split(b, '?'))
    d = str.join('.',str.split(c, '!'))
    resolucao=str.count(d,".")
    return resolucao