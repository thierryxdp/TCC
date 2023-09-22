def soma_h(N):
    ''' esta função calcula o somatório de frações com n termos onde cada fração
    tem o denominador igual a sua posição no somatório.
    int --> float'''
    lista_soma = [1]
    
    for numero in range(2,N +1):
        lista_soma.append((numero)**-1)
    somatorio = sum(lista_soma)
    
    return round(somatorio, 2)