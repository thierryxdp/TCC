def uppCons(frase):
    '''Recebe uma frase e retorna uma nova com todos as consoantes da frase original maiusculas;str->str'''
    
   
    i=0
    fraseNova=''
    letra=frase[i]
    
    while i<len(frase):
        if letra in 'bcdfghjklmnpqrstvwxyz':
            letra = str.upper(letra)
        fraseNova = fraseNova + letra    
        i=i+1
    return fraseNova