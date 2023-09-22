def inverte(frase):
    pontuacao=(",","-",":",".","!","?")
    frase=str.replace(frase,str((",","-",":",".","!","?"))," ")
    frase=str.lower(frase)
    frase=list.reverse(list(frase))
    return frase