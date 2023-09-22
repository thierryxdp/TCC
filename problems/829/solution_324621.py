def soma_h(n):
    lista_soma = {1}
    for numero in range (2, n+1):
        lista_soma.append((numero)**-1)
    somatorio = sum(lista_soma)
    return round(somatorio, 2)