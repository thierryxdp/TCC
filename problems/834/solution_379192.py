def media_matriz(matriz):
    '''Função que retorna a média de 
    uma matriz
    list -> float'''
    divisor = len(matriz) * len(matriz[0])
    soma = 0
    
    for linha in range(len(matriz)):
        
        for indice in range(len(matriz[linha])):
            soma = soma + matriz[linha][indice]
            
    divisor = soma/divisor
    arredonda = round(divisor, 2)
    return arredonda