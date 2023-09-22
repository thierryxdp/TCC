def lingua_p(termo):
    
    '''
    Função que recebe uma frase e retorna a mesa traduzida na língua do P
    com todas as letras minúsculas.

    str -> str
    '''
        
    minuscula = str.lower(termo)
    traduzido = ''
    
    for i in range(0,len(minuscula)):
        if minuscula[i] in 'bcdfghjklmnpqrstvwxyzç':
            traduzido += minuscula[i]
        else:
            traduzido += minuscula[i] + 'p' + minuscula[i]
    	
    return traduzido