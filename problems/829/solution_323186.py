def soma_h(N):
    "retorna a soma da expressão H"
    soma = 0
    for i in range(1, N+1):
        soma = soma + 1/ i
    return round(soma,2)