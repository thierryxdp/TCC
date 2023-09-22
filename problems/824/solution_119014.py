def uppCons(frase):
    '''função que retorna a frase com suas consoantes
    em termo maiúsculo
    str -> str'''
    
    Q = len(frase)
    nova_frase = ''
    i = 0
    
    while i < Q :
        if frase[i] in 'bçcdfghjklmnpqrstvwxyz':
            nova_frase = nova_frase+str.upper(frase[i])
        else :
                nova_frase = nova_frase+frase[i]
        i = i + 1
    return nova_frase