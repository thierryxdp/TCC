def uppCons (frase):
    '''Função que retorna a frase com todas as consoantes em 
    maiúsculas. str->str'''
    r = ''
    consoantes = 'bcdfghjklmnpqrstvwxyzç'
    
    for caractere in frase:
        if caractere in consoantes:
            r += caractere.upper()
        else:
            r += caractere
    return r