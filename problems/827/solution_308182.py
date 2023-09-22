def qtd_divisores(n):
    #Calcula a quantidade de divisores de um numero
    #Entrada: n ; saida: divisores
    divisores = 0
    for i in range(1, n + 1):
        if n % i == 0:
            divisores += 1

    return divisores