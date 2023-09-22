def uppCons(frase):
    '''recebe frase e retorna a mesma com as consoantes em maiúscula'''
    '''string -> string'''
    
    i=0
    modificada=''
    
    while i < len(frase):
        a=frase[i]
        if a in 'bcçdfghijklmnpqrstvwxyz':
            a=str.upper(a)
        modificada=modificada+a
        i=i+a
        
    return modificada