def uppCons(frase):
    '''Recebe uma frase e retorna uma nova com todos as consoantes da frase original maiusculas;str->str'''
    
   
    i=0
    fraseNova=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase[i]=str.upper(frase[i])
        fraseNova=fraseNova+frase[i]    
        i=i+1
    return fraseNova