def soma_h(n):
    '''calcula e retorna o valor h com N termos onde N é inteiro
    int -> float'''
    soma = 1
    for i in list(range(1, n + 1)):
        soma = soma + (1 / i)
        
    return round(soma, 2)