frase=str.replace(frase,'.',' ')
    frase=str.replace(frase,',',' ')
    frase=str.replace(frase,'-',' ')
    frase=str.replace(frase,'?',' ')
    frase=str.replace(frase,'!',' ')
    frase=str.replace(frase,':',' ')
    frase=str.replace(frase,';',' ')
    return frase

def inverte(frase):
    '''recebe uma frase e retorna uma outra frase com as mesma palvras na ordem inversa, sem letras maiúsculas e sem a pontuação
    str->str'''
    frase=frase
    frase=str.lower(frase)
    frase=retira_pontuacao(frase)
    frase=str.split(frase)
    list.reverse(frase)
    return str.join(' ',frase)