def uppCons(frase):
    '''
    Recebe uma  string, verfica se é uma string e,
    Retorna uma string contendo as consoantes em maíusculo e as vogais em minúsculo
    '''
    s = ''
    
    for caractere in frase:
        if caractere in 'bcdfghjklmnpqrstvxwyz':
            s += caractere.upper() 
        else: 
            s += caractere
    return s