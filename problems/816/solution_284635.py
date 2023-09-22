def maiores (lista,numero):
    indice = 0
    resultado = []
    while indice < len(lista):
        elemento = lista[indice]
        
        if elemento > numero:
            resultado.append(elemento)
        indice += 1
    return resultado.sort()