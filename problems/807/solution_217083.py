def conta_frases(texto):
    '''função que conta numero de frases no texto:
    str -> tupla'''
    Int = texto.count("?")
    pont = texto.count(".")
    exc = texto.count("!")
    ret = texto.count("...")
    ret = texto.count("...")*3
    return (Int + pont + exc + ret)= ret