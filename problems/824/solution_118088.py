def uppCons(frase):
    '''
    '''
    
    i=0
    frase2=''
    
    while i<len(frase):
        
         if frase[i] in ' B C D  F G H  J K L M N  P Q R S T  V W X Y Zb c d f g h j k l m n p q r s t v w x z':
                frase2=frase2+frase[i]
         
         if frase[i] in 'aeiouAEIOU':
                frase2=frase2+frase[i]
           
         i+=1
    
    return frase2