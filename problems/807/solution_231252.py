def conta_frases(texto):
    frase1=str.count(texto,".")
    frase2=str.count(texto,"?")
    frase3=str.count(texto,"!")
   
    return frase1+frase2+frase3