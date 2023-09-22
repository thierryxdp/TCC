def soma_h(n):
    '''função que a partir de um número inteiro n retorna uma soma h no formato h = 1 + 1/2 + 1/3 + 1/4 + ... + 1/n,
    com duas casas decimais de precisão.
    int -> float'''
    
    soma=0
    
    for numero in range(n+1):
        soma = soma + (1/numero)
    return round(soma, 2)