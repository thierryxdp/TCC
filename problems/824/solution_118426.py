def uppCons(frase):
    '''função que retorna uma dada frase de entrada com todas as suas consoantes maiúsculas
    str -> str'''
    fraseCons = ''
    for cons in frase:
        if cons in 'bcçdfghjklmnpqrstvwxyzBCÇDFGHJKLMNPQRSTVWXYZ'
           fraseCons += cons.upper()
        else:
            fraseCons += cons
    return fraseCons