def soma_h(n:int)->float:
    '''retorna a soma da função H (soma das frações 1 sobre 1 até
    1 sobre n) onde n é o valor dado como parâmetro.'''
    soma = 0
    for numero in range(1,n+1):
        soma = soma + 1/numero
    return round(soma, 2)