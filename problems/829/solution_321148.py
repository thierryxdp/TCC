def soma_h(n):
    '''Calcula e retorna o valor de H
       com n termos;
       int -> float'''
    soma = 0
    for i in range(0,n+1):
        num=1/n
        soma = soma + num 
    return round(soma,2)