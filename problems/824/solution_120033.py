def uppCons(frase):
    '''Função que retorna uma frase com todas as suas consoantes maiúsculas, dada uma frase normal
    str -> str'''
    i=0
    x=''
    while i<len(f):
        if f[i] in 'bcdfghjklmnpqrstvwxyz':
        	x=x+str.upper(f[i])
        else:
            x=x+f[i]
        i=i+1
    return x