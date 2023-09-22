def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna a mesma traduzida 
    para a língua do P. str->str'''
    
    palavra_parametro=''
    
    for l in palavra:
        if l in 'aeiouAEIOUáâãéêôóú':
            palavra_parametro+= l+'p'+l
        else:
             palavra_parametro+=l
        
    return palavra_parametro