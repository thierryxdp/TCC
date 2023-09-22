def faltante(lista):
    lista.sort()
    comparar = range(1,len(lista)+2)
    contador=0
    lista.append('')
    while contador <= len(lista):
        if lista[contador]!=comparar[contador]:
            return comparar[contador]
        if  comparar[contador]==comparar[-1]:
            return comparar[contador]+1
        
        contador+=1
        
p