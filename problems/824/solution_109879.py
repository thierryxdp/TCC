def uppCons(frase):
    '''Esta função retorna a frase inserida com todas 
    as consoantes em maísculo
    str -> str'''
    
    nova_frase=''
    indice = 0
    
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante=str.upper(frase[indice])
            nova_frase=nova_frase + frase[:indice]+consoante+frase[indice+1:]
            
        indice= indice + 1
        
    return nova_frase