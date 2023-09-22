def acima_da_media (lista):
    indice = 0
    resultado = []
    while indice < len(lista):
        elemento = lista[indice]
        
        if elemento > ((sum(lista))/len(lista)):
            resultado.append(elemento)
        indice += 1
        resultado.sort()
    return resultado