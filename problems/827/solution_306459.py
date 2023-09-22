def qtd_divisores(numero):
    ''' Função que dado um número, calcula a quantidade
    de divisores que tal número possui.
    Entrada: int
    Retorno: int '''
    
    soma = 0
    for x in range(1,numero+1):
        if (numero%x) == 0:
            soma = soma + 1
    return soma