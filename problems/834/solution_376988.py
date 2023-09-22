def media_matriz(matriz):
    '''Função que recebe uma matriz inteira não vazia e retorna a média de
todos os numeros com duas casas decimais'''
    soma = 0.0
    tamanho = 0.0

   
    for linha in matriz:
        
        for elemento in linha:
            
            soma += elemento
            
            tamanho += 1.0

    
   

    
    return round(soma/tamanho,2)