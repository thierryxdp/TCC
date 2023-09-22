def soma_h(n):
    '''Função que recebe um inteiro e calcula o valor H com
    Ntermos, onde N é inteiro.
    int -> float'''
    
    soma = 0
    
    for x in range(1, n+1):
        soma = soma + 1/x

    return round(soma, 2)