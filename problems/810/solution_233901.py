def subst_espaco(texto):
    '''str -> str'''
    return str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(str.replace(texto,'...',' '),'?',' '),'!',' '),'.',' '),';',' '),':',' '),',',' '),'-',' ')

def inverte(frase):
    '''Função, que dada uma frase, retorna essa frase invertida, sem letras maiúsculas e sem pontuação
    str -> str'''
    return str.lower(str.join(' ',(str.split(subst_espaco(frase))[::-1])))