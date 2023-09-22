def uppCons(frase):
    '''função que recebe uma frase e retorna ela com todas as consoantes maiúsculas; str=>str'''
    i=0
    nova="
    while i<len(frase):
        a=frase[i]
        if a in 'bcçdfghjklmnpqrstvwxyz':
            a=str.upper(a)
        nova=nova+a
        i=i+1
    return nova