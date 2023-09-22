def uppCons(frase):
    '''funçao que recebe uma frase e retorna a mesma frase com todas as suas consoantes em maiusculo'''
    '''str -> str'''
    
    i=0
    retorno=''
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
        retorno=retorno+frase[i]
        i=i+1
           
    return retorno