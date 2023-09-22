def posLetra(texto,letra,n):
    i=str.index(texto, letra)
    if letra in texto:
        if n==1:
            return i
        elif n > 1:
            return str.find(texto,letra,i)