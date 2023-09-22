def uppCons(frase):
    '''recebe uma frase e retorna a mesma só que com todas as consoantes em maiusculo
    str->str'''
    i=0   
    while i < len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvxwyz':
            up = str.upper(frase[i])
            nova_frase = str.replace(frase,frase[i],up)
            frase = nova_frase
        i=i+1
    return frase