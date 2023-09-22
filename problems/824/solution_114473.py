def uppCons(frase):
    
    '''Função que a partir de uma frase de entrada, retorna a mesma frase, porém com todas as consoantes em maiúsculas. str -> str'''
    
    i = 0
    retorno = ''
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzç':
            retorno = retorno + str.upper(frase[i])
        else:
            retorno = retorno + frase[i]
        i = i + 1
    
    return retorno