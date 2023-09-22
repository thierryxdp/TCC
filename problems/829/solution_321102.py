def soma_h(n):
    '''Calcula a soma de H com n termos
    int -> float'''
    soma = 1
    for i in (2,n+1):
        soma += 1 / i 
    return round(soma,2)