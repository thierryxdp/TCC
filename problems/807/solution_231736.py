def conta_frases(frase):
    '''Calcule e retorne uma função que conta e o numero de frases que aparecem no texto'''
    
    i = str.count(frase, "!")
    e = str.count(frase, "?")
    r = str.count(frase, "...") #1
    s2 = str.replace(s2, "...","")
    pf = str.count(s2,".")
    
    return e + i + r + pf