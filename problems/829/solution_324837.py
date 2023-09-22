def soma_h(N):
    soma = []
    for elemento in range(2,N+1):
        soma.append((elemento)**-1)
    total = sum(soma)
    return round(total,2)