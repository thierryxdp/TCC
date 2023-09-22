def soma_h(n):
    '''função que, dado um valor n, retorna o valor H com n termos; 
    int -> float'''
    soma=0
    for i in range(1,n+1):
        soma=soma + 1/i
    return round(soma,2)