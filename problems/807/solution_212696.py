def conta_frases(texto):
    '''dado um texto, retorna o número de frases contido nele;
    str -> int'''
    
    texto2 = str.replace(texto,'...','3pts')
    ponto = str.count(texto2,'.')
    exclamacao = str.count(texto2,'!')
    interrogaçao = str.count(texto2,'?')
    reticencias = str.count(texto2,'3pts')
    quantidade = ponto + exclamacao + interrogacao + reticencias
    
    return quantidade