def uppCons(frase):
    '''
       Função que retorna uma frase com todas
       as suas consoantes MAIÚSCULAS
       str->str
    '''
    
    i=0
    frase2=list(frase)
    lfinal=[]
    
    while i<len(frase):
        if frase2[i] in 'cbdfghjklmnpqrstvwxyzç':
            frase2.insert(i,frase[i].upper())
            
    i+=1
         
         else:
            lfinal.insert(i,frase[i])
    i+=1
    
    return lfinal in ''