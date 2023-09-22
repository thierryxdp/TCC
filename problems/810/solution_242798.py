def inverte(frase):
    lista = str.split(frase)
    lista.reverse()
    
    #lista = list.reverse(frase)
    
    frase = str.join(" ", lista)
    return frase