def soma_h(n):
    '''calcula e retorna o valor de H com N termos, onde N é inteiro e dado como entrada e 
    H = 1 + 1/2 + 1/3 + ... + 1/n
    int -> float'''
    soma = 1
    for i in range (1, n+1):
        soma = soma + 1/n
    return round(soma, 2)