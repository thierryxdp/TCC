def ex4(frase,palavra,posicao):
    lista = frase.split(" ")
    if palavra in lista:
        pos = lista.index(palavra)
        lista[pos] = lista[pos].upper()
        return str.join(" ",lista)
    else:
        lista.insert(posicao,palavra)
        return str.join(" ",lista)