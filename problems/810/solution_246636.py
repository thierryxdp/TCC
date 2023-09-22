def inverte(frase):
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "-"," ")
    frase = str.replace(frase, "  "," ")
    
    frase = str.lower(frase)
    
    palavras = str.split(frase," ")
    
    invertida = palavras[::-1]
    
    str.join(invertida)