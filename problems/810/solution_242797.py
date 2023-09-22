def inverte(frase):
    lista = str.split(frase)
    lista.reverse(frase)
    
    #lista = list.reverse(frase)
    
    frase = str.join(" ", lista)
    return frase