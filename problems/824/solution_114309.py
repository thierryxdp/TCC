def uppCons(frase):
    '''retorna todas as consoantes da frase maiúsculas;
    str -> str'''
    
    i = 0
    maiu=''
    
    while i < len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            maiu = maiu + str.upper(frase[i])
            
        i=i+1
        
        frase = str.replace(frase,'i',maiu)
    return frase