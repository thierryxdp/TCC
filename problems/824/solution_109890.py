def uppCons(frase):
    '''Esta função retorna a frase inserida com todas 
    as consoantes em maísculo
    str -> str'''
    
    nova_frase=''
    indice= 0
    
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante=str.upper(frase[indice])
            nova_frase=replace(frase,frase[indice],consoante)
            
        indice= indice + 1
        
    return nova_frase