def inverte(frase):
    frase = str.replace(frase, "."," ")
    frase = str.replace(frase, ","," ")
    frase = str.replace(frase, "!"," ")
    frase = str.replace(frase, "?"," ")
    frase = str.replace(frase, "-"," ")
    palavras = str.split(frase," ")
    invertida = ' '.join(palavra[::-1] for palavra in frase.split())invertida = ' '.join(palavras[::-1] for palavras in frase)
    
    return str.lower(invertida)