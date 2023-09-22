def posLetra(frase,letra,ocorrencia):
    lista = []
    contador_lista = 0
    while contador_lista < len(frase):
        lista = list.append(lista,frase[contador_lista])
        contador_lista += 1
    if letra not in frase or list.count(lista,letra) < ocorrencia:
        return -1
    contador = 0
    while contador <= ocorrencia:
        list.index(lista,letra)
        contador += 1
    return contador