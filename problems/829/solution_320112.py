def soma_h(n):
    '''
        Função que retorna o valor H com N termos.
        Int => Int    
    '''
    soma = 0
    for i in range(1,n+1):
        soma += 1/i
    soma = round(soma, 2)
    return soma