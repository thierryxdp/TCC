def soma_h(n):
    "dado um numero n de termos, calcula o somatório da série"
    somatorio = 0
    for fracao in range(1,n+1):
        somatorio += 1/fracao
    return round(somatorio,2)