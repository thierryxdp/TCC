def somaFatorial(n):
    soma = 0
    for numero in range(1,n+1):
        soma += factorial(numero)
    return soma