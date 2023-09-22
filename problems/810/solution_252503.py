def inverte(frase):
    frase = str.replace(frase,".","")
    frase = str.replace(frase,",","")
    frase = str.replace(frase,"?","")
    frase = str.replace(frase,"!","")
    frase = str.replace(frase,"-"," ")
    lista = str.split(frase)
    lista.reverse()
    frase = str.join(" ", lista)
    frase = str.lower(frase)
    return frase