def uppCons (frase):
    '''função em que dada uma frase retorne a mesma frase com todas as suas
    consoantes em maiúsculo;
    str -> str'''
    i=0
    frase1=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
            frase1=frase1+strupper(frase[i])
        else: #quando não for consoante
            frase1=frase1+frase[i]
        i=i+1
    return frase1