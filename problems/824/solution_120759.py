def uppCons(frase):
    '''Recebe uma frase e retorna uma nova com todos as consoantes da frase original maiusculas;str->str'''
    
    fraseNova=''
    i=0
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            fraseNova = fraseNova + str.upper(frase[i])
        i=i+1
    return fraseNova