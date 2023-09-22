def qtd_divisores(numero):
    ''' Função que dado um número, calcula a quantidade
    de divisores que tal número possui.
    Entrada: int
    Retorno: int '''
    
    soma = 0
    for x in range(numero+1):
        if (x%2) == 0:
            soma = soma +1
    return soma