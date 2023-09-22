def soma_h(N):
    ''' '''
    numerador=1
    denominador=1
    H=1
    for i in range(1,N+1):
        numerador=1
        denominador+=1
        numero=numerador/denominador
        H+=numero
    return round(H,2)