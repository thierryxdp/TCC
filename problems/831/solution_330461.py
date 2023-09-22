def lingua_p(palavra):
    
    vogal='aeiou'
    linguap=''
    
        
    for letra in palavra:
        if palavra[letra]==vogal:
            linguap=linguap+'p'+palavra[letra]
        return linguap