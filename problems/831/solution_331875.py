def lingua_p(palavra):
    '''
       Função que retorna string com a palavra traduzida na lingua do p
       
       str->str
    '''
    final=''
    
    for i in range(len(palavra)):
        if palavra[i] in 'aeiouáéíóú':
            final+=palavra[i]+'p'+palavra[i]
        
        else:
            final+=palavra[i]
            
    return final