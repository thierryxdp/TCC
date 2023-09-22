def soma_h(n):
    '''calcula e retorna o valor h com N termos onde N é inteiro
    int -> float'''
    soma = 1
    for i in list(range(n)):
        soma = soma + (1 / n)
        
    return round(soma, 2)