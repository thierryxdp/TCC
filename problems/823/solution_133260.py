def faltante(lista):
    lista.sort()
    listaRetorno = []
        
    for i in lista:
        if lista[i] != list(range(lista[len(lista) - 1]))[i]:
            listaRetorno.append(i)
        
    return int(listaRetorno[0])