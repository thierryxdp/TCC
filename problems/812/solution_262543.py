def retira_pontuacao(string):
    '''Função que recebe uma string e retorna ela sem nenhum caracter de pontuação.
    Esses caracteres serão substituídos por espaço. str->str'''
    a=string.replace('!','')
    b=a.replace('...','')
    c=b.replace('?','')
    d=c.replace(';','')
    e=d.replace('-','')
    f=e.replace(':','')
    g=f.replace(',','')
    return g