def lingua_p(palavra):
    
    vogal='aeiou'
    linguap=palavra
    
        
    for cachorro in range(len(palavra)):
        if palavra[cachorro] in vogal:
            linguap=linguap+'p'+palavra[cachorro]
    return linguap