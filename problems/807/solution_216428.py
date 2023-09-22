def conta_frases(frase):
    ret='...'
    if frase.find(ret):
        x = frase.count(ponfinal)+frase.count(ret)-3+frase.count("!")+frase.count("?")
        return (x)
    else: 
        ponfinal = '.'
        x = frase.count(ponfinal)+frase.count("!")+frase.count("?")
        return (x)