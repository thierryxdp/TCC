def soma_h(n):
    '''retorna o valor de H com N termos, em que N é inteiro
    int-> float'''
    soma = 0
    for i in range(1, n+1):
        soma = soma + (1/i)
    return round(soma, 2)