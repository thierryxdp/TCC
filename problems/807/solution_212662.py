def conta_frases(texto):
    """ função que conta o número de frases que aparecem no texto, podendo ser separadas por ponto final, de exclamação, interrogação ou reticencias"""
    x= str.split(texto,".")
    y= str.split(str(x,"!"))
    z= str.split(str(y,"?"))
    w= str.split(str(z,"..."))
    return len(w)