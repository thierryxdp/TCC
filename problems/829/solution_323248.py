def soma_h(n):
    '''recebe um n e retorna o valor de h, sendo n termos.
    int -> float
    explicação: basta circular o valor i e fazer a soma como o H dado.'''
    soma=0
    for i in range(1,n+1):
        soma=soma+1/i
    return round(soma,2)