def posLetra(texto,letra,n):
    cont = 0
    lista = []
    while cont < len(texto):
        if letra in texto:
            lista += [texto.index(letra)]
        else:
            return -1
        cont = cont + 1
    return lista[n-1]