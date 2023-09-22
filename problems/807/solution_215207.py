def conta_frases(frase):
    str.replace('; ', ', ')
    #frase = str.strip(frase)
    frase = str.split(frase,".")
    x = len(frase)
    return(x-1)