def media_matriz(matriz):
    '''Calcula e retorna a média de todos os números da 
       matriz dada;
       list -> float'''
    
    numeros = 0
    soma = 0
    
    for linha in matriz:
        
        for coluna in matriz:
            
            numeros += 1
            soma += coluna
            
    return soma / numeros