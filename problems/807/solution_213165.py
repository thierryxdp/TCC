def conta_frases(texto): 
    '''dado um texto a função calcula o número de frases que aparecem nele'''
    return str.count(texto,"!")+ str.count(texto,"?")+ str.count(texto,".")+ str.replace(texto,".")