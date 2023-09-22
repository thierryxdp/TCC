def qtd_divisores(numero):
    '''Funcao que retorna a quantida de 
    divisores que o numero de entrada tem.
    Dados de entrada = int
    Valor de saida = int
    '''
    quantidade = 0 
    for divisor in range(1,1+numero):
        if numero % divisor == 0:
            quantidade += 1
    return quantidade