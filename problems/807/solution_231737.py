def conta_frases(s):
    '''Calcule e retorne uma função que conta e o numero de frases que aparecem no texto'''
    
    i = str.count(s, "!")
    e = str.count(s, "?")
    r = str.count(s, "...") #1
    s2 = str.replace(s2, "...","")
    pf = str.count(s2,".")
    
    return e + i + r + pf