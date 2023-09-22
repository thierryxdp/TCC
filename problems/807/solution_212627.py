def conta_frases(texto):
    """ função que conta o número de frases que aparecem no texto, podendo ser separadas por ponto final, de exclamação, interrogação ou reticencias"""
    x= str.split(texto,".")
    y= str.split(x,"!")
    z= str.split(y,"?")
    w= str.split(z,"...")
    return len(w)