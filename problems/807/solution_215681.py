def conta_frases(frase):
    x = str.count(frase,".")
    y = str.count(frase,"!")
    z = str.count(frase,"?")
    i = str.count(frase,"...")
    j = str.count(frase,",")
    k = str.count(frase,";")
    
    return x + y +z + w - j - k