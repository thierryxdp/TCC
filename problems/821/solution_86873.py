def fatorial(n):
    '''Função que dado um número
    calcula o fatorial desse numero.
    Dados de entrada: int 
    Valor de saída: int
    '''
    fat = 1
    while n > 1:
        fat *= n
        n -= 1
    return fat