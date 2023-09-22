def conta_frases(frase):
  
    f = 0  
    if '!' in frase:
        f = f + str.count(frase,"!")
    if '?' in frase:
        f = f + str.count(frase,"?")
    if '.' in frase:
        f = f + str.count(frase,".") 
    if '...' in frase:
        f = f + str.count(frase,".")*3 - str.count(frase,".")
    return f