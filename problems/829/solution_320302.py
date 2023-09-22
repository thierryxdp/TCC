def soma_h(N):
    '''Calcula e retorna a soma dos N termos, tal que, cada termo é o inverso de um inteiro
       parameters:
       N: Numero de termos colocados na soma
       int-> float'''
    proximo=1
    soma=0
    for proximo in range(1,N+1):
        soma = soma + proximo ** -1
        proximo=proximo+1
    return round(soma,2)