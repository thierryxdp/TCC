def uppCons(frase):
    '''Recebe uma frase e retorna uma nova com todos as consoantes da frase original maiusculas;str->str'''
    
   
    i=0
    fraseNova=''
    
    while i<len(frase):
        letra=frase[i]
        if letra in 'bcdfghjklmnpqrstvwxyzç':
            letra = str.upper(letra)
        fraseNova = fraseNova + letra    
        i=i+1
    return fraseNova