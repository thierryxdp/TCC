def uppCons(frase):
    '''Função que retorna uma frase com todas as suas consoantes maiúsculas, dada uma frase normal
    str -> str'''
    i=0
    x=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyz':
        	x=x+str.upper(frase[i])
        else:
            x=x+frase[i]
        i=i+1
    return x