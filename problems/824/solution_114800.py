def uppCons(frase):
    '''funçao que recebe uma frase e retorna a mesma frase com todas as suas consoantes em maiusculo'''
    '''str -> str'''
    
    i=0
    retorno=''
    
    while i < len(frase):
        a=frase[i]
        if a in 'bcdfghjklmnpqrstvwxyzç':
            a=str.upper(a)
        retorno=retorno+a
        i=i+1
           
    return retorno