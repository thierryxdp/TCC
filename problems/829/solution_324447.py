def soma_h(N):

    lista_soma = [1]
    for numero in range(2, N+1):
        lista_soma.append((numero)**-1)
        
    return round(somatorio, 2)
        somatorio = sum(lista_soma)