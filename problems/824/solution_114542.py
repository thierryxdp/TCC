def uppCons(frase):
    ''' funcao recebe uma frase e transforma todas as consoantes
    dessa frase em maiuscula, str-->str'''
    i=0
    s=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvxwyz':
            s+= frase[i].upper()
        else:
            s+=frase[i]
        i=i+1    
            return s