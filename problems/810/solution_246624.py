def inverte(frase):
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "-"," ")
    palavras = str.split(frase," ")
    invertida = ' '.join(palavras[::-1] for palavras in frase.split())invertida = ' '.join(palavras[::-1] for palavras in frase)
    
    return str.lower(invertida)