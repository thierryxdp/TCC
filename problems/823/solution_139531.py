def faltante(lista):
    lista.sort()
    comparar = range(1,len(lista)+2)
    contador=0
    while contador < len(lista):
        if lista[contador]!=comparar[contador]:
            return comparar[contador]
        contador+=1