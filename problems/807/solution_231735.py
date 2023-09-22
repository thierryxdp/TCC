def conta_frases(frase):
    '''Calcule e retorne uma função que conta e o numero de frases que aparecem no texto'''
    
    i = str.count(frase, "!")
    e = str.count(frase, "?")
    r = str.count(frase, "...") #1
    frase2 = str.replace(frase2, "...","")
    pf = str.count(frase2,".")
    
    return e + i + r + pf