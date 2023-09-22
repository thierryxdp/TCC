def posLetra(texto,letra,n):
    cont = 0
    while cont < len(texto):
        if letra in texto:
            return texto.find(letra,n)
        else:
            return -1