def inverte(frase)
lista = str.split(frase)
    lista.reverse()
    #lista = list.reverse(lista)
    frase = str.join(" ", lista)
    return frase