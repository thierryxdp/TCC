def uppCons(frase):
    '''Esta função retorna a frase inserida com todas 
    as consoantes em maísculo
    str -> str'''
    
    indice= 0
    nova_frase=''
    
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante=str.upper(frase[indice])
            nova_frase=str.replace(nova_frase,frase[indice],consoante)
            
        indice= indice + 1
        
    return nova_frase