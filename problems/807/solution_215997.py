def conta_frases(paragrafo):
    '''Função que dado um paragrafo onde as frases são separadas pelas 
    pomtuações: ponto final, ponto de esclamação, ponto de interrogação 
    ou reticências retorna a quantidade de frases;
    srt->int'''
    
    if '...' in paragrafo:
        return str.count(paragrafo,'!') + str.count(paragrafo,'?') + ((str.count(paragrafo,'.')- 2)* str.count(paragrafo,'...'))
    else:
        return str.count(paragrafo,'.') + str.count(paragrafo,'!') + str.count(paragrafo,'?')