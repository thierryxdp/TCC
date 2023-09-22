def retira_pontuacao(x):
    '''retorna a frase dada sem os caracteres de pontuação, no lugar deles, retorna um espaço. str->str'''
    if '.' in x:
        x=str.replace(x,'.',' ')
    if ',' in x:
        x=str.replace(x,',',' ')
    if ':' in x:
        x=str.replace(x,':',' ')
    if ';' in x:
        x=str.replace(x,';',' ')
    if '-' in x:
        x=str.replace(x,'-',' ')
    if '?' in x:
        x=str.replace(x,'?',' ')
    if '!' in x:
        x=str.replace(x,'!',' ')
    return x