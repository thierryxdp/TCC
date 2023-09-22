def uppCons(frase):
    '''funçao que recebe uma frase e retorna a mesma frase com todas as suas consoantes em maiusculo'''
    '''str -> str'''
    
    i=0
    retorno=''
    
    while i < len(frase):
        maiusculo=frase[i]
        if a in 'bcdfghjklmnpqrstvwxyzç':
            maiusculo=str.upper(maiusculo)
        retorno=retorno+maiusculo
        i=i+1
           
    return retorno