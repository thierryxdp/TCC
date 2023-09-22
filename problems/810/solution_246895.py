def inverte(frase):
    frase.replace(',','')
    frase.replace('.','')
    frase.replace('!','')
    frase.replace('?','')
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    return frase