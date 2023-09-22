def posLetra(texto,letra,n):
    cont = 0
    proximo = 0
    qtd = texto.count(letra)
    lista = []
    while cont < len(texto):
        if qtd < n:
            return -1
        if texto[cont] == letra:
            lista = lista + [texto.index(texto[proximo])]  
        cont = cont + 1
        proximo += 1
    return lista[n-1]