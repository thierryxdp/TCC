def media_matriz(m):
    '''
       Função que retorna a média dos numeros de uma matriz 
       int/list->float
    '''
    
    soma=0
    final=0
    
    for imatriz in m:
        for i in imatriz:
            soma+=i
            final+=1
            
    M=soma/final       
            
    return round(M,2)