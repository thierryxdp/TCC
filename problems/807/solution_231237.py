def conta_frases(texto):
    frase1=str.split(texto,".")
    frase2=str.split(frase1,"#")
    frase3=str.split(frase2,"?")
    frase4=str.split(frase3,"...")
    return frase2