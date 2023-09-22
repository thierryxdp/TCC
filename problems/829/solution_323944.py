def soma_h(n):
    '''retorna o valor h com n termos onde n é inteiro'''
    soma = 0 
    for i in range(1, n+1):
        H = 1/i
        soma += H 
        return round(soma, 2)