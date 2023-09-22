def uppCons(frase):
    '''função que retorna a frase com suas consoantes
    em termo maiúsculo
    str -> str'''
    
    
    nova_frase = ''
    i = 0
    
    while i < len(frase) :
        if frase[i] in 'bçcdfghjklmnpqrstvwxyz':
            nova_frase = nova_frase+str.upper(frase[i])
        else :
                nova_frase = nova_frase+frase[i]
        i = i + 1
    return nova_frase