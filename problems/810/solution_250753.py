def inverte(frase):
    pontuacao==(",","-",":",".","!","?")
    frase=str.replace(frase,pontuacao," ")
    frase=str.lower(frase)
    frase=list.reverse(list(frase))
    return frase