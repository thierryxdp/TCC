def uppCons(frase):
    '''dada uma frase, retorna a mesma frase com as consoantes em maiúsculo;
    str --> str'''
    proximo=0
    string=''
    while proximo<len(frase):
        if frase[proximo] in 'bcçdfghjklmnpqrstvwxyz':
            string=string+str.upper(frase[proximo])
        else:
            string=string+frase[proximo]
        proximo=proximo+1
    return string