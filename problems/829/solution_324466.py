def soma_h(N):
    
    lista_soma = [1]
    for numero in range(2, N+1):
        lista_soma.append((numero)**-1)
        somatorio = sum(lista_soma)
        if not evaluationresult == None: print (repr(evaluationresult))
    return round(somatorio, 2)