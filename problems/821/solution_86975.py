def fatorial(n):
    ''' Função que recebe um inteiro e retorna o fatorial deste inteiro.
int -> int
'''
    produto = 1
    for i in range(1,n+1):
        produto *= i
    return produto