def uppCons(frase):
    '''Recebe uma frase e retorna uma nova com todos as consoantes da frase original maiusculas;str->str'''
    
   
    i=0
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
        i=i+1
    return frase