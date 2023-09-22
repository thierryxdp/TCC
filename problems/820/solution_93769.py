def posLetra(frase,letra,numero):
    if (list.count(list(frase),letra))<numero:
        return -1
    lista = []
    proximo = 0
    while proximo<len(frase):
        if str(letra) in frase[proximo]:
            retornar = list.pop(list(frase),numero)
    	proximo = proximo + 1
    return list.index(retornar,letra)