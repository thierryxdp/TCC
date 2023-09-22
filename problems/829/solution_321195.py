def soma_h(n):
    '''Retorna o valor H com N termos onde N é inteiro e dado como entrada;
    int -> float'''
    soma = 0
    for c in range(1, n+1):
        inverso = (1/c)
        soma += inverso
    return round(soma, 2)