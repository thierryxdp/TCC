def uppCons(frase):
    '''retorna a frase fornecida com todas as suas 
    consoantes em maiusculas; str -> str'''
    frase_nova=frase[:]
    i=0
    while i<len(frase):
        if frase[i] in 'bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ':
            frase_nova=str.replace(frase_nova,frase_nova[i],str.upper(frase[i]))
        i=i+1
    return frase_nova