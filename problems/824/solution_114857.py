def uppCons(frase):
    '''recebe frase e retorna a mesma com as consoantes em maiúscula'''
    '''string -> string'''
    
    i=0
    nova=''
    
    while i < len(frase):
        a=frase[i]
        if a in 'bcçdfghijklmnpqrstvwxyz':
            a=str.upper(a)
 
        nova=nova+a
        i=i+1
        
    return nova