def soma_h ( n ) :
    soma = 0
    c1 = 0
    while ( c1 < n ) :
        numerador = 1
        denominador = c1 + 1
        elemento = numerador / denominador
        soma += elemento
        c1 += 1
    return round(soma,2)