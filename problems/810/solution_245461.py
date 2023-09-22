def retira_pontuacao(string):
    '''Função que recebe uma string e retorna ela sem nenhum caracter de pontuação.
    Esses caracteres serão substituídos por espaço. str->str'''
    a=string.replace('!',' ')
    b=a.replace('...',' ')
    c=b.replace('?',' ')
    d=c.replace(';',' ')
    e=d.replace('-',' ')
    f=e.replace(':',' ')
    g=f.replace(',',' ')
    h=g.replace('.',' ')
    return h
def so_inverte(frase):
    '''Função que recebe uma frase e apenas a inverte. str->str'''
    return frase[::-1]
def inverte(frase):
    '''Função que recebe uma frase dada como entrada e retorna uma outra frase
    que contenha as mesmas palavras dela só que na ordem inversa, sem letras maiúsculas,
    e sem a pontuação. str->str'''
    frase_invertida=so_inverte(frase)
    frase_sem_pontuacao=retira_pontuacao(frase_invertida)
    frase_minuscula=frase_sem_pontuacao.lower
    return frase_minuscula