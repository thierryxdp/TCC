def posLetra(frase,letra,numero):
    if (list.count(list(frase),letra))<numero:
        return -1
    lista = []
    vezes = 0
    proximo = 0
    while proximo<len(frase):
        if str(letra) in frase[proximo]:
            adicionar = (list(frase)).index(letra)
            lista.append(adicionar)
            
            vezes = vezes + 1
    	proximo = proximo + 1
    return lista