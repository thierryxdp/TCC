def soma():
    soma = 0
    denominador = 1

    for i in range (10,0,-1):
        soma += float(i)/factorial(denominador)
        denominador += 1
    return soma