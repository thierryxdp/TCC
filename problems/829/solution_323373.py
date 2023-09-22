def soma_h(n):
    '''calcula a soma de n termos dada a função 1+1/n'''
    soma = 0
    for c in range(1, n + 1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)