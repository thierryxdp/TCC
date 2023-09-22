def inverte(frase):
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, "  "," ")
    
    frase = str.lower(frase)
    
    palavras = str.split(frase," ")
    
    invertida=palavras.reverse()
    return invertida
    #return str.join(" ",invertida)