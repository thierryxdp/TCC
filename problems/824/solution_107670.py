def uppCons(frase):
    '''Retorna uma frase com todas suas consoantes em maiuscula.
       str -> str'''
    i=0
    consoantes=''
    while i<len(frase):
        if frase[i] in 'çbcdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ':
            consoantes = consoantes + str.upper(frase[i])
            i=i+1
        else:
            consoantes = consoantes + frase[i]
            i=i+1
            
    return consoantes