def soma_h(n):
    '''  
Função que a calcula e retorna o valor H com N termos, 
onde N  ́e inteiro e  ́e dado como entrada.
    int-->float
    '''
    acumulador=0
    for i in range(1,n+1):
        
        acumulador=acumulador+1/i
        
    return round(acumulador,2)