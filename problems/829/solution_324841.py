def soma_h(N):
    '''funcao calcula as somas das fracoes'''
    '''int--> float'''
    l_s = [1]
    for numero in range(2, N+1):
        l_s.append((numero)**-1)
    somatorio = sum(lista_soma)
    return round(somatorio, 2)