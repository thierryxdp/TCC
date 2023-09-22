def conta_frases (frase):
    '''dado um texto, a função retorna o número de frases que aparecem no texto.
    frase (str)--> número de frases (int)'''
    x = str.replace(frase, ('!'), '.')
    y = str.replace(x, ('...'), '.')
    z = str.replace(y, ('?'), '.')
 
    return str.count(z,".")