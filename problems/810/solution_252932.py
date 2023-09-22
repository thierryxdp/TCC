def inverte(frase):
    '''Função que inverte a ordem das palavras de uma frase sem pontuação'''
    frase = str.replace(frase,'.',' ')
    frase = str.replace(frase,',',' ')
    frase = str.replace(frase,';',' ')
    frase = str.replace(frase,':',' ')
    frase = str.replace(frase,'!',' ')
    frase = str.replace(frase,'?',' ')
    frase = str.replace(frase,'-',' ')
    l = str.split(frase,' ')
    return str(l[−1]) + ' ' + str(l[2]) + ' ' + str(l[−3])