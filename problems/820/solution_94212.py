def posLetra(texto,letra,n):

    m=str.index(texto, letra)
    if letra in texto:
        if n==1:
            return m
        elif n > 1:
            return str.find(texto, letra, m+1)