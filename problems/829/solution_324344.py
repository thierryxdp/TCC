def soma_h(n):
    '''funcao que calcula e retorna o valor h com n termos onde n é inteiro e dado como entrada, 
    retornando o resultado com 2 casas decimais; int -> float'''
    
    acumulador = 0
    
    for i in range(1, n + 1):
        
        h = 1/i
        
        acumulador += h
        
    return round(acumulador,2)