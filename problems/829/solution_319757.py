def soma_h(N):
    '''calcula o valor H do número dado com entrada, sendo:
    H = 1+ 1/2 + 1/3 + ... + 1/N;
    int -> float'''
    soma = 0
    for denominador in range(1,N+1):
        soma += 1/denominador
    return round(soma,2)