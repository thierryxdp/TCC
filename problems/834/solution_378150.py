def media_matriz(matriz):
    '''Calcula e retorna a média de todos os números da 
       matriz dada;
       list -> float'''
    
    numeros = 0
    soma = 0
    
    for linha in matriz:
        
        for coluna in linha:
            
            numeros += 1
            soma += coluna
            
    return round(soma / numeros,2)