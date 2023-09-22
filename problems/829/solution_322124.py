def soma_h(N):
    """ Função que calcula o valor de H = 1 + 1/2 + ... + 1/N
        com N termos onde N é inteiro e dado como parâmetro;
        int -> float"""
    soma = 0
    for i in range(1,N+1):
        soma = soma + (1/i)
    return round(soma,2)