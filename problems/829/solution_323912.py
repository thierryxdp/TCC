def soma_h(n):
    '''Dado N, calcula e retorna o valor de H com N termos''' 
    soma = 0
    for i in range(1, n + 1):
        inverso = (1/i)
        soma += inverso
    return round(soma, 2)