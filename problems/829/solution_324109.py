def soma_h(n):
    soma = 0
    for num in range(n+1):
        if num != 0:
            soma += 1/num
    return round(soma,2)