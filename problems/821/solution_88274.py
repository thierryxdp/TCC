def fatorial(num):
    "retorna o fatorial do numero de entrada"
    fact = 1
    for n in range(1, num + 1, 1):
        fact *= n
    return fact