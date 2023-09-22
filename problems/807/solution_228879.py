def cont_frases(umafrase):
    """função que calcula os numeros das freses apresentado 
    no texo trazento um solução positiva na resolução do problema"""
    b = str.join('.',str.split(numfrases,'...')
    c = str.join('.',str.split(b, '?'))
    d = str.join('.',str.split(c, '!'))
    resolucao=str.count(d,".")
    return resolucao