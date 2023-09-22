def faltante(lista):
    
    i=0
    resultado=0
    ordenada=sorted(lista)
    lista_modificada=list(range(1, (ordenada[-1]+1)))

    while i < len(lista):
        if ordenada[i] != lista_modificada[i]:
            retorno=lista_modificada[i]
             i=lista[0:-1]
        else:
            retorno=lista_modificada[i]+1
            i=i+1
    return retorno