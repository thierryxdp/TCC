def uppCons(frase):
    '''Retorna a frase com as consoantes em caixa alta;
    str->str'''
    
    i=0
    
    while i<len(frase):
        if frase[i]=='bcdfghjklmnpqrstvwxyz':
            str.upper(frase[i])
        i+=1