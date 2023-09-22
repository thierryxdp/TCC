def inverte(frase):
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    frase = str.replace(frase,".","")
    return frase