def lingua_p(palavra):
    
    vogal='aeiou'
    linguap=''
    
        
    for cachorro in range(len(palavra)):
        if palavra[cachorro] in vogal:
            linguap=linguap+'p'+palavra[cachorro]
            
        if palavra[cachorro] not in vogal:
            linguap=linguap+palavra[cachorro]
            
        
    return linguap