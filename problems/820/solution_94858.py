def posLetra(texto,letra,n):
    cont = 0
    qtd = texto.count(letra)
    lista = []
    while cont < len(texto):
        if texto[cont] == letra:
            lista += [texto.index(texto[cont])]
        if qtd < n:
            return -1  
        cont = cont + 1
    return lista