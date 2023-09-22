def retira_pontuacao (texto):
    '''função que recebe uma frase retorna uma
    frase onde todos os caracteres de pontuação são
    substituidos por espaço'''
    texto = texto.replace('-',' ')
    texto = texto.replace(',','')
    texto = texto.replace(':','')
    texto = texto.replace('!','')
    texto = texto.replace('...','')
    texto = texto.replace('?','')
    texto = texto.replace('.','')
    return texto


def inverte (frase):
    '''função que recebe uma frase
    retoruna uma frase que contenha as mesmas 
    palavras na ordem inverse, sem letras
    maiuscular e sem a pontuação'''
    f=retira_pontuacao(frase)
    f=str.lower(f)
    f=f.strip(' ')
    f=f.split(' ')
    f=f[::-1]
    a=' '
    f=a.join(f)
    return f