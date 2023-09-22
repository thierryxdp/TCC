def inverte(frase):
    lista = str.split(frase)
    lista.reverse(sem pontuação)
    
    #lista = list.reverse(frase)
    
    frase = str.join(" ", lista)
    return frase