def cont_frases(umafrases):
    """função que calcula os numeros das freses apresentado 
    no texo trazento um solução positiva na resolução do problema"""
    b = str.join('.',str.split(umafrases,'...')
    c = str.join('.',str.split(b, '?'))
    d = str.join('.',str.split(c, '!'))
    resolucao=str.count(d,".")
    return resolucao