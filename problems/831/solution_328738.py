def lingua_p(palavra):
    '''Função que recebe uma palavra e retorna a mesma traduzida 
    para a língua do P. str->str'''
    
    palavra_parametro=''
    
    for l in palavra:
        if l in 'aeiouAEIOUáâãêôóú':
            oalavra_parametro+= letra+'p'+letra
        else:
             palavra_parametro+=letra
        
    return palavra_parametro