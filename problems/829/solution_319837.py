def soma_H(n):
    Soma = 0
    for i in range(1,n):
        Soma = Soma + 1/i
    return round(Soma,2)