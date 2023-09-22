def soma_h(n):
    '''Função que recebe um número inteiro e calcula a expressão onde
    h é a variável.
    tipo de entrada: int
    tipo de saída: bool'''
    
    h = 0
    for i in range(1, n+1):
        h = h + 1/i
    return round(h, 2)