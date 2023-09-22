def soma_h(n):
    '''dado um numero inteiro retorna o valor de total de uma soma com n termos
    int-> float'''
    total=0
    for i in range(1,n+1):
        total+=1/i
    return round(total,2)