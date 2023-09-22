def posLetra(texto,letra,n):
    cont = 0
    qtd = texto.count(letra)
    lista = []
    while cont < len(texto):
        if qtd < n:
            return -1
        if texto[cont] == letra:
            lista += [texto.index(texto[cont])]  
        cont = cont + 1
    return lista[n-1]