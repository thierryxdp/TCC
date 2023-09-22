def lingua_p(palavra):
    
    vogal='aeiou'
    linguap=''
    
        
    for cachorro in range(len(palavra)):
        if palavra[cachorro]==vogal:
            linguap=linguap+palavra[cachorro]+'p'
    return linguap