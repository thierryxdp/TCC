def inverte(frase):
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, "  "," ")
    
    frase = str.lower(frase)
    
    palavras = str.split(frase)
    palavras.reverse() 
    invertida = " ".join(palavras)

    return invertida