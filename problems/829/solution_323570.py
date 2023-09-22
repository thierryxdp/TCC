def soma_h(N):
    '''Retorna o valor de H, dado N como entrada;
    int->float'''
    numerador=1
    denominador=1
    H=1
    for i in range(1,N):
        denominador+=1
        numero=numerador/denominador
        H+=numero
    return round(H,2)