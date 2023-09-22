def uppCons(frase):
    '''Função que recebe como entrada uma frase e retorna a frase com todas as suas consoantes em maiúsculas; str -> str'''
    i=0
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvxywz':
            str.upper(frase[i])
        i=i+1
    return frase