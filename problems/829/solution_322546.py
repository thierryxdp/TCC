def soma_h(n):
    '''retorna o resultado com 2 casas decimais'''
    soma=0
    for c in range (1,n+1):        
        inverso=(1/c)       
        soma+=inverso        
    return round(soma,2)