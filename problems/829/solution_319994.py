def soma_h(n):
    '''calcula e retorna o valor H com N termos onde N é o parametro de entrada.
    int -> float'''
    soma = 0
    for X in range(1,n+1):
        soma += (1/X)
    return round(soma,2)