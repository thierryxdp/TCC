def uppCons(frase):
    '''Dada uma frase, retorna a mesma frase com todas as suas consoantes em maiusculas.
    str -> str'''
    i=0
    frasenova=''
    while i<len(frase):
        if frase[i] in 'bcdfghjklmnpqrstvwxyzçBCDFGHJKLMNPQRSTVWXYZÇ':
            frasenova=frasenova+str.upper(frase[i])
        else:
        	frasenova=frasenova+frase[i]
        i=i+1
    return frasenova