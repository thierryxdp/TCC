def conta_frases(frase):
    ret='...'
    ponfinal = '.'
    if frase.find(ret):
        x = frase.count(ret)+frase.count("!")+frase.count("?")
        return (x)
    else: 
        x = frase.count(ponfinal)+frase.count("!")+frase.count("?")
        return (x)