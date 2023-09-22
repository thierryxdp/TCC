def uppCons(frase):
    '''Esta função retorna a frase inserida com todas 
    as consoantes em maísculo
    str -> str'''
    
    indice= 0
    
    while indice<len(frase):
        if frase[indice] in 'bcdfghjklmnpqrstvwxyz':
            consoante=str.upper(frase[indice])
            lista_frase=str.split(frase,' ')
            list.insert(lista_frase,indice,consoante)
            s=''
            teste=s.join(lista_frase)
        indice= indice + 1
        
    return teste