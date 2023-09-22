def soma_h(n):
    '''Retornar o valor H com N termos, onde N é inteiro e é dado como entrada;
    int -> float'''
    
    soma = 0
    for x in range(1, n+1):
        soma += 1/x
    
    return round(soma, 2)