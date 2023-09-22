def soma_h(n):
    '''Função que dado um numero inteiro n, retorna o valor de 
    H(expressão dada na questão) com n termos.
    int -> float'''
    H= 0
    for x in range(1, n+1):
        soma= 1/x
        H= H + soma
    return round(H,2)