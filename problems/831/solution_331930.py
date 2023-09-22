def lingua_p(palavra):
    '''traduz a palavra(em português) para a língua do P
    	str->str'''
    
    palavra_P=''
    
    for i in range(len(palavra)):
        
        if palavra[i] in 'AEIOUÁÉÍÓÚaeiouáéíóú':
            
            palavra_P=palavra_P+palavra[i]+'p'+palavra[i]
            
        else:
            
            palavra_P=palavra_P+palavra[i]
     
    return palavra_P