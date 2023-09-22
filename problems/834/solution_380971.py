def media_matriz(m):
    '''funcao que retorna a media de todos os numeros da matriz list -> float'''
    
    soma = 0
    
    valores = 0
    
    for coluna in m:
        
        for elemento in coluna:
            
            soma = soma + elemento
            
            valores = valores + 1
    
    return round(soma/valores,2)