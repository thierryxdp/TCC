def uppCons(frase):
    '''recebe uma frase e a retorna com todas as suas consoantes em
    maiúsculas.
    str -> str'''
    
    i=0
    frase_nova=''
    
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase_nova=frase_nova+str.replace(frase,frase[i],str.upper(frase[i]))
        i=i+1
    return frase_nova