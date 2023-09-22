def soma_H(n):
    soma=0
    numeros=1
    for i in range(n+1):
        if i>=1:
            soma=soma+numeros/i
    return round(soma,2)