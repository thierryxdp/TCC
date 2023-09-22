def conta_frases(texto):
    '''uma função que conta o número de frases em um texto cujo o termino consiste em ponto final,
    um ponto de exclamação, ponto de interrogação ou reticências.
    str -> tupla'''
    frases=[]
    str.find(texto,'!')+=frases
    str.find(texto,'?')+=frases
    str.find(texto,'...')+=frases
    str.find(texto,'.')+=frases
    return frases