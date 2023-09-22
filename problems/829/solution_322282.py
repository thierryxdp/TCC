def soma_h(N):
    ''' dando N numeros inteiros retorna a soma H desses numeros.
    sendo 1 + 1/2+...'''
    numero = 0
    
    for i in range(1,N+1):
        numero = numero +1/i
    return round(numero, 2)