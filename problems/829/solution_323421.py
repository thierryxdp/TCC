def soma_h(n):
    '''função que recebe um valor inteiro n e retorna o valor de h com
    n termos. O resultado deve ser retornado com apenas 2 casas decimais.
    entrada:int
    saída:float'''
    h=0
    for i in range(1,n+1):
        h = h + (1/i)
 
    return round(h,2)