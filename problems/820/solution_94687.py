def posLetra(texto,letra,n):
    cont = 0
    qtd = texto.count(letra)
    while cont < len(texto):
        if letra in texto:
            if qtd >= n:
                index = texto.find(letra,n)
            	return index
            else:
                return -1
        cont = cont +1
    return index