def soma_h(n):
    '''função que dada um numero inteiro n, calcula e retorna 
    o valor de h com n termos. int --> float'''
    num = 1
    y=2
    num2 = 1/y 
    h = 0
    
    for x in range(n):
        h = num + num2
        y = y+1
        
    return round(h, 2)