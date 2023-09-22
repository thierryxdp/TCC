def lingua_p(palavra):
    
    vogal='aeiou'
    linguap=''
    
        
    for indice in range(len(palavra)):
        if palavra[indice] in vogal:
            linguap=linguap+palavra[indice]+'p'+palavra[indice]
            
        if palavra[indice] not in vogal:
            linguap=linguap+palavra[indice]
            
        
    return linguap