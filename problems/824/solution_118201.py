def uppCons(frase):
    '''
       Função que retorna uma frase com todas
       as suas consoantes MAIÚSCULAS
       str->str
    '''
    
    i=0
    frase2=''
    while i<len(frase):
        if frase[i] in 'cbdfghjklmnpqrstvwxyzç':
            frase2=frase[i].upper()
            
    i+=1
            
         else:
            frase2=frase[i]
            
    i+=1
    
    
    return ''+frase2