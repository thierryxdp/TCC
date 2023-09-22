def inverte(frase):
    frase = str.lower(frase)
    frase = str.replace(frase, ",", "")
    frase = str.replace(frase, ".", "")
    list = str.split(frase, )
    liste = list.reverse()
    
    return liste