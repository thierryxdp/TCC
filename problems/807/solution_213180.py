def conta_frases(texto): 
    '''dado um texto a função calcula o número de frases que aparecem nele'''
   texto= texto.replace('...' ,'.')
    return str.count(texto,"!")+ str.count(texto,"?")+ str.count(texto,".")