def uppCons(frase):
    '''
    '''
    
    i=0
    frase2=''
    
    while i<len(frase):
        
         if frase[i] in 'b c d f g h j k l m n p q r s t v w x z':
                frase2+=frase[i]
                str.upper(frase2)
          
         
         i+=1
    
    return frase2