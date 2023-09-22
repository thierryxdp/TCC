def posLetra(frase,letra,numero):
    i = 0
    lista = []
    while i<len(frase):
        if frase[i] == letra:
            lista.append(i)
            i+=1
        else:
            i+=1
    if numero <= len(lista):
        return lista[numero-1]
    else:
        return -1