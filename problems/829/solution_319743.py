def soma_h(N):
    '''Retorna o valor da soma H com N termos com 2 casas decimais;
    int -> float'''
    soma=0
    for i in range(1,N+1):
        soma=soma+1/i
    return round(soma,2)